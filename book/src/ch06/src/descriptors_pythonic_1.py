"""Clean Code in Python - Chapter 6: Descriptors

> First example: the naive implementation using properties
"""


class Traveler:
    """A person visiting several cities.

    We wish to track the path of the traveller, as he or she is visiting each
    new city.
    """

    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]

    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)
        self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited
