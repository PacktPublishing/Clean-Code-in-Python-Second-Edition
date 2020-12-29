"""Clean Code in Python - Chapter 9: Common Design Patterns

 > Composite
"""

from typing import Iterable, Union


class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price


class ProductBundle:
    def __init__(
        self,
        name: str,
        perc_discount: float,
        *products: Iterable[Union[Product, "ProductBundle"]]
    ) -> None:
        self._name = name
        self._perc_discount = perc_discount
        self._products = products

    @property
    def price(self) -> float:
        total = sum(p.price for p in self._products)  # type: ignore
        return total * (1 - self._perc_discount)
