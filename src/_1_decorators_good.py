from base import logger


# 2. with decorators

def db_status_handler(db_script_function):
    def inner(cursor):
        commands = db_script_function(cursor)
        function_name = db_script_function.__qualname__
        try:
            for command in commands:
                cursor.execute(command)
        except Exception as e:
            logger.exception("Error in %s: %s", function_name, e)
            return -1
        else:
            logger.info("%s run successfully", function_name)
            return 0
    return inner


@db_status_handler
def update_db_indexes(cursor):
    return (
        """REINDEX DATABASE transactional""",
    )


@db_status_handler
def move_data_archives(cursor):
    return (
        """INSERT INTO archive_orders SELECT * from orders
        WHERE order_date < '2016-01-01' """,
        """DELETE from orders WHERE order_date < '2016-01-01' """,
    )
