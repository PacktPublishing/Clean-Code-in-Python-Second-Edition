"""Clean Code in Python - Chapter 5: Decorators

Composition over inheritance, example 1
"""
from dataclasses import dataclass


def _resolver_method(self, attr):
    """The resolution method of attributes that will replace __getattr__."""
    if attr.startswith("resolve_"):
        *_, actual_attr = attr.partition("resolve_")
    else:
        actual_attr = attr
    try:
        return self.__dict__[actual_attr]
    except KeyError as e:
        raise AttributeError from e


def with_resolver(cls):
    """Set the custom resolver method to a class."""
    cls.__getattr__ = _resolver_method
    return cls


@dataclass
@with_resolver
class Customer:
    customer_id: str
    name: str
    address: str
