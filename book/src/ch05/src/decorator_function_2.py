"""Clean Code in Python - Chapter 5: Decorators

Example for the first section: the decorator doesn't allow parameters.
> Function decorators
    - Creating a decorator to be applied over a function.
    - Implement the decorator as an object.
"""
from functools import wraps

from decorator_function_1 import ControlledException
from log import logger


class Retry:
    def __init__(self, operation):
        wraps(operation)(self)
        self.operation = operation

    def __call__(self, *args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return self.operation(*args, **kwargs)
            except ControlledException as e:
                logger.info("retrying %s", self.operation.__qualname__)
                last_raised = e
        raise last_raised


@Retry
def run_operation(task):
    """Run the operation in the task"""
    return task.run()
