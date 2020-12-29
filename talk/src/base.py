import logging
from enum import Enum
from collections import namedtuple


logger = logging.getLogger(__name__)


class DBCursor:
    def __init__(self):
        self._calls = []

    def execute(self, command):
        self._calls.append(command)


###############################

def run(*ars):
    print(ars)


def stop_database_service():
    print("Stopping database service")
    run("systemctl stop postgres")


def start_database_service():
    print("Starting database service")
    run("systemctl start postgres")


def run_offline_db_backup():
    print("Running backup on database...")
    print("Backup finished")

###############################################################################

Coord = namedtuple('Coord', 'x, y')


class OutOfBoundaryException(Exception):
    """Raised when trying to access a coordinate that is out of the boundaries
    of the map"""


class GameStatsLogger(object):
    def log_action(self, msg):
        self._send_log_msg(msg)


class Element(Enum):
    EMPTY = 0

    @classmethod
    def units_count(cls):
        return 0


class Unit(Enum):
    DEFAULT = 0

    @classmethod
    def units_count(cls):
        return 1


class MapBoundary(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __contains__(self, coord):
        return 0 <= coord.x < self.height and 0 <= coord.y < self.width


class Map(object):

    def __init__(self, height, width):
        self.grid = [
            [Element.EMPTY for __ in range(height)]
            for __ in range(width)]
        self.boundaries = MapBoundary(height=height, width=width)

    def __getitem__(self, coord):
        if coord in self.boundaries:
            return self.grid[coord.x][coord.y]
        raise OutOfBoundaryException()


class MapView(object):
    def __init__(self, grid):
        self.grid = grid

    def item_is_in_coord(self, coord, item):
        return self.grid[coord] == item

    def coord_is_empty(self, coord):
        return self.grid[coord] == Element.EMPTY


class User:
    pass

class Product:
    def __init__(self, id_, count=0):
        self.id = id_
        self.count = count


class Category:
    def __init__(self, products=None):
        self.products = products or []


class Stock:
    def __init__(self, categories=None):
        self.categories = categories or []
        self._products_by_category = {}

    @property
    def products_by_category(self):
        pass

    def __contains__(self, product):
        for category in self.categories:
            for prod in category.products:
                if prod.count > 0 and prod.id == product.id:
                    return True
        return False

    def request(self, product):
        pass


class Customer:
    def assign_product(self, product):
        pass
