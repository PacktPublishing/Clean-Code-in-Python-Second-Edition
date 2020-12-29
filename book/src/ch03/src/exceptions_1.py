"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Error Handling - Exceptions
"""
import logging
import time

from base import Connector, Event

logger = logging.getLogger(__name__)


class DataTransport:
    """An example of an object handling exceptions of different levels."""

    _RETRY_BACKOFF: int = 5
    _RETRY_TIMES: int = 3

    def __init__(self, connector: Connector) -> None:
        self._connector = connector
        self.connection = None

    def deliver_event(self, event: Event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        except ConnectionError as e:
            logger.info("connection error detected: %s", e)
            raise
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise

    def connect(self):
        for _ in range(self._RETRY_TIMES):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(
                    "%s: attempting new connection in %is",
                    e,
                    self._RETRY_BACKOFF,
                )
                time.sleep(self._RETRY_BACKOFF)
            else:
                return self.connection
        raise ConnectionError(
            f"Couldn't connect after {self._RETRY_TIMES} times"
        )

    def send(self, data: bytes):
        return self.connection.send(data)
