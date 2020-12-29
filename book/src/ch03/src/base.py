"""Clean code in Python - Chapter 03
Common definitions
"""


class Connector:
    """Abstract the connection to a database."""

    def connect(self):
        """Connect to a data source."""
        return self

    @staticmethod
    def send(data):
        return data


class Event:
    def __init__(self, payload):
        self._payload = payload

    def decode(self):
        return f"decoded {self._payload}"
