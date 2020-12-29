"""Clean Code in Python - Chapter 5: Decorators

Simplified calls for decorators with default arguments.
"""
from functools import wraps, partial

DEFAULT_X = 1
DEFAULT_Y = 2


def decorator(function=None, *, x=DEFAULT_X, y=DEFAULT_Y):
    if function is None:
        return partial(
            decorator, x=x, y=y
        )  # also lambda f: decorator(f, x=x, y=y)

    @wraps(function)
    def wrapped():
        return function(x, y)

    return wrapped
