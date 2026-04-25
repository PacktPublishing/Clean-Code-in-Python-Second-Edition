"""Clean Code in Python - Chapter 5: Decorators

Parametrized decorators using functions
"""

from functools import wraps
from typing import Sequence, Optional, Type

from decorator_function_1 import ControlledException
from log import logger


_DEFAULT_RETRIES_LIMIT = 3


def with_retry(
    retries_limit: int = _DEFAULT_RETRIES_LIMIT,
    allowed_exceptions: Optional[Sequence[Type[Exception]]] = None,
):
    allowed_exceptions = allowed_exceptions or (ControlledException,)  # type: ignore

    def retry(operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None
            for _ in range(retries_limit):
                try:
                    return operation(*args, **kwargs)
                except allowed_exceptions as e:
                    logger.warning(
                        "retrying %s due to %s", operation.__qualname__, e
                    )
                    last_raised = e
            raise last_raised

        return wrapped

    return retry
