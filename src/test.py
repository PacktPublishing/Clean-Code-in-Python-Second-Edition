import pytest
import contextlib
import os
import io

from base import MapView, Map, Coord, OutOfBoundaryException
from base import DBCursor

from base import Product, Stock, Customer, Category

import _0_meaning_bad
import _0_meaning_good

import _1_decorators_bad
import _1_decorators_good

import _2_context_managers

import _3_properties

import _4_magics_bad
import _4_magics_good

import _5_idioms


@pytest.fixture
def standard_game_map():
    return Map(width=5, height=5)


@pytest.fixture
def cursors():
    return DBCursor(), DBCursor()


class ErroneousCursor(DBCursor):
    def execute(self, *args):
        raise Exception()


class MockedDict(dict):
    def set(self, key, value):
        self[key] = value


@pytest.fixture
def player_status(mocker):
    mocker.patch('redis.StrictRedis')
    player_status = _3_properties.PlayerStatus()
    player_status.redis_connection = MockedDict()
    return player_status


class TestMeaning:
    """Tests for section 0: meaningful code"""

    def _printed_lines(self, function, year):
        """call the function, and count the number of lines on its output"""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            function(year)
        txt = output.getvalue()
        return len(txt.splitlines())

    @pytest.mark.parametrize(
        'elapse_function',
        (_0_meaning_bad.elapse, _0_meaning_good.elapse)
    )
    @pytest.mark.parametrize('year', (range(2013, 2016)))
    def test_elapse(self, elapse_function, year):
        """call with non-leap years"""
        assert self._printed_lines(elapse_function, year) == 365

    @pytest.mark.parametrize(
        'elapse_function',
        (_0_meaning_bad.elapse, _0_meaning_good.elapse)
    )
    @pytest.mark.parametrize('year', (range(2000, 2020, 4)))
    def test_elapse_leap(self, elapse_function, year):
        """Call with leap years"""
        assert self._printed_lines(elapse_function, year) == 366


class TestMagic:

    @pytest.mark.parametrize('function', (
        _4_magics_bad.request_product_for_customer,
        _4_magics_good.request_product_for_customer,
    ))
    def test_product_not_in_stock(self, function):
        result = function(
            Customer(),
            Product(id_='1', count=0),
            Stock()
        )
        assert result == "Product not available"

    @pytest.mark.parametrize('function', (
        _4_magics_bad.request_product_for_customer,
        _4_magics_good.request_product_for_customer,
    ))
    def test_product_in_stock(self, function):
        product = Product(id_='1', count=10)
        stock = Stock(categories=[
            Category([product, product]),
            Category([product]),
        ])
        assert function(Customer(), product, stock) is None


class TestImplementationDetails:
    """Test for the section of implementation details"""

    def test_original(self, player_status):
        assert player_status.points == 0
        player_status.accumulate_points(100)
        assert player_status.points == 100

    def test_improved(self, player_status):
        assert player_status.points == 0
        player_status.points += 44
        assert player_status.points == 44


class TestContextManager:
    """Tests for the slides about maintaining state
    with context managers
    """

    @pytest.mark.parametrize('function', (
        _2_context_managers.test_first_backup,
        _2_context_managers.offline_db_backup)
    )
    def test_context_manager_called(self, mocker, function):
        enter = mocker.patch('_2_context_managers.stop_database_service')
        exit = mocker.patch('_2_context_managers.start_database_service')

        function()

        assert enter.called
        assert exit.called


class TestMap:
    def test_map_boundaries(self, standard_game_map):
        map_vision = MapView(standard_game_map)
        item = '*' * 4
        coord = Coord(0, 0)

        assert map_vision.item_is_in_coord(coord, item) is False
        assert map_vision.coord_is_empty(coord)

    def test_map_out_of_limits(self, standard_game_map):
        map_vision = MapView(standard_game_map)
        with pytest.raises(OutOfBoundaryException):
            map_vision.item_is_in_coord(Coord(99, 99), None)


class TestDuplication:
    """Test the decorators examples"""

    def test_non_repeated_function(self, cursors):
        cur1, cur2 = cursors
        _1_decorators_bad.update_db_indexes(cur1)
        _1_decorators_good.update_db_indexes(cur2)
        expected = ["""REINDEX DATABASE transactional"""]
        assert cur1._calls == cur2._calls == expected

    def test_second_decorator(self, cursors):
        cur1, cur2 = cursors
        _1_decorators_bad.move_data_archives(cur1)
        _1_decorators_good.move_data_archives(cur2)
        expected = [
            """INSERT INTO archive_orders SELECT * from orders
            WHERE order_date < '2016-01-01' """,
            """DELETE from orders WHERE order_date < '2016-01-01' """,
        ]
        assert cur1._calls == cur2._calls
        calls = [' '.join(stm.split()) for stm in cur2._calls]
        exp_calls = [' '.join(stm.split()) for stm in expected]
        assert calls == exp_calls

    @pytest.mark.parametrize('function', (
        _1_decorators_bad.move_data_archives,
        _1_decorators_good.move_data_archives,
        _1_decorators_bad.update_db_indexes,
        _1_decorators_good.update_db_indexes,
    ))
    def test_exception_handled(self, function):
        cursor = ErroneousCursor()
        status = function(cursor)
        assert status == -1


class TestIdioms:
    """Tests for section 5: idioms & common patterns"""

    def _rm_test_file(self):
        with contextlib.suppress(FileNotFoundError):
            os.remove(_5_idioms.DATA_FILE)

    def _create_test_file_with_content(self, content):
        with open(_5_idioms.DATA_FILE, 'w+') as f:
            f.write(content)

    @pytest.mark.parametrize(
        'counting_function',
        (
            _5_idioms.count_words_1,
            _5_idioms.count_words_2,
            _5_idioms.count_words_3,
        )
    )
    def test_count_words(self, counting_function):
        words = (
            "Acquaintance", "Rendezvous",
            "Acquaintance", "House", "Trip", "House", "House")
        expected_count = {
            'Acquaintance': 2,
            'Rendezvous': 1,
            'House': 3,
            'Trip': 1,
        }
        assert counting_function(words) == expected_count

    @pytest.mark.parametrize(
        'function',
        (_5_idioms.ignore_exceptions_1, _5_idioms.ignore_exceptions_2)
    )
    def test_ignoring_exceptions_file_not_found(self, function):
        self._rm_test_file()
        assert function() is None

    @pytest.mark.parametrize(
        'function',
        (_5_idioms.ignore_exceptions_1, _5_idioms.ignore_exceptions_2)
    )
    def test_ignoring_exceptions_file_found(self, function):
        self._create_test_file_with_content("test")
        assert function() == "test"
        self._rm_test_file()

    @pytest.mark.parametrize(
        'function',
        (
            _5_idioms.find_first_even_1,
            _5_idioms.find_first_even_2,
            _5_idioms.find_first_even_3,
        )
    )
    def test_first_event_present(self, function):
        expected = 88
        assert function(87, 97, 79, 88, 3, 2, 55) == expected

    @pytest.mark.parametrize(
        'function',
        (
            _5_idioms.find_first_even_1,
            _5_idioms.find_first_even_2,
            _5_idioms.find_first_even_3,
        )
    )
    def test_first_event_not_present(self, function):
        assert function(1, 3, 5, 7, 9) is None
