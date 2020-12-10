"""
Examples of the application of Python decorators in order to
reduce code duplication.
It presents first, the naïve approach, with duplicated code,
and then, the improved solution using decorators.
"""
from base import logger


def decorator(original_function):
    def inner(*args, **kwargs):
        # modify original function, or add extra logic
        return original_function(*args, **kwargs)
    return inner


# 1. Repeated
def update_db_indexes(cursor):
    commands = (
        """REINDEX DATABASE transactional""",
    )
    try:
        for command in commands:
            cursor.execute(command)
    except Exception as e:
        logger.exception("Error in update_db_indexes: %s", e)
        return -1
    else:
        logger.info("update_db_indexes run successfully")
        return 0


def move_data_archives(cursor):
    commands = (
        """INSERT INTO archive_orders SELECT * from orders
        WHERE order_date < '2016-01-01' """,
        """DELETE from orders WHERE order_date < '2016-01-01' """,)
    try:
        for command in commands:
            cursor.execute(command)
    except Exception as e:
        logger.exception("Error in move_data_archives: %s", e)
        return -1
    else:
        logger.info("move_data_archives run successfully")
        return 0
