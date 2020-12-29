"""Clean Code in Python - Chapter 3: General Traits of Good Code

> Error Handling - Exceptions
"""
import logging
import time

from base import Connector, Event

logger = logging.getLogger(__name__)


def connect_with_retry(
    connector: Connector, retry_n_times: int, retry_backoff: int = 5
):
    """Tries to establish the connection of <connector> retrying
    <retry_n_times>, and waiting <retry_backoff> seconds between attempts.

    If it can connect, returns the connection object.
    If it's not possible to connect after the retries have been exhausted, raises ``ConnectionError``.

    :param connector:         An object with a ``.connect()`` method.
    :param retry_n_times int: The number of times to try to call
                                ``connector.connect()``.
    :param retry_backoff int: The time lapse between retry calls.

    """
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(
                "%s: attempting new connection in %is", e, retry_backoff
            )
            time.sleep(retry_backoff)
    exc = ConnectionError(f"Couldn't connect after {retry_n_times} times")
    logger.exception(exc)
    raise exc


class DataTransport:
    """An example of an object that separates the exception handling by
    abstraction levels.
    """

    _RETRY_BACKOFF: int = 5
    _RETRY_TIMES: int = 3

    def __init__(self, connector: Connector) -> None:
        self._connector = connector
        self.connection = None

    def deliver_event(self, event: Event):
        self.connection = connect_with_retry(
            self._connector, self._RETRY_TIMES, self._RETRY_BACKOFF
        )
        self.send(event)

    def send(self, event: Event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise
