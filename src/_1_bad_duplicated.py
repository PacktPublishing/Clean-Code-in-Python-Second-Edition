"""
Example of a bad design, with duplicated code and logic.
The code is for educational purposes, in order to show how it can be refactored
or abstracted in a much better way.
"""
from base import OutOfBoundaryException
from base import Element


def item_is_in_coord(grid, coord, item):
    if 0 <= coord.x < grid.height and 0 <= coord.y < grid.width:
        return grid[coord.x][coord.y] == item
    return OutOfBoundaryException()


def coord_is_empty(grid, coord):
    if 0 <= coord.x < grid.height and 0 <= coord.y < grid.width:
        return grid[coord.x][coord.y] == Element.EMPTY
    raise OutOfBoundaryException()

######################################################################

def item_is_in_coord(grid, coord, item):
    return grid[coord] == item

def coord_is_empty(grid, coord):
    return grid[coord] == Element.EMPTY

######################################################################

map_vision = MapView(grid)
map_vision.item_is_in_coord(coord, item)
map_vision.coord_is_empty(coord)


######################################################################


def item_is_in_coord(grid, coord, item):
    return grid[coord] == item


def coord_is_empty(grid, coord):
    return grid[coord] == Element.EMPTY

######################################################################



## 1. bad
def exchange_user_points(user, item):
    if user.points >= 100 and user.account_enabled:
        if user.points >= item.required_points:
            user.points -= item.required_points
            user.items.append(item)


def show_item_catalogue_to_user(user, category):
    if user.points >= 100 and user.account_enabled:
        category_view = "menu_{}.html".format(category)
        user.history.append(category_view)
        return (user, category_view)


def f1():
    if x > 1 and y > 2:
        customer = Customer(name="John", last_name="Smith")
        customer.apply_charges()
        return Registration(customer=customer)


def f2():
    if x > 1 and y > 2:
        cart = ShoppingCart(products=("product1", "product2"))
        cart.evaluate_items()
        return cart


def preconditions_met():
    return x > 1 and y > 2


## 2. still not good enough
def f1():
    if preconditions_met():
        customer = Customer(name="John", last_name="Smith")
        customer.apply_charges()
        return Registration(customer=customer)


def f2():
    if preconditions_met():
        cart = ShoppingCart(products=("product1", "product2"))
        cart.evaluate_items()
        return cart
## 3. better
def _preconditions_met():
    return x > 1 and y > 2

def preconditions_met(function):
    def inner(*args, **kwargs):
        if _preconditions_met():
            return function(*args, **kwargs)
    return inner

@preconditions_met
def f1():
    customer = Customer(name="John", last_name="Smith")
    customer.apply_charges()
    return Registration(customer=customer)


@preconditions_met
def f2():
    cart = ShoppingCart(products=("product1", "product2"))
    cart.evaluate_items()
    return cart


######################################################################

def custom_transaction1():
    with TransactionalState(*conn_args):
        t1 = Transaction(from_='x', to='y')
        t1.start(state)
        t1.process()
        t1.stop()
        return t1.status
