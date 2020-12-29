import pytest
from coverage_caveats import my_function


@pytest.mark.parametrize("number,expected", [(2, "even")])
def test_my_function(number, expected):
    assert my_function(number) == expected
