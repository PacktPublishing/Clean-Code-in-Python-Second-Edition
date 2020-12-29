import contextlib
from base import start_database_service, stop_database_service, run_offline_db_backup

###################################################


class DBHandler:
    def __enter__(self):
        stop_database_service()
        return self

    def __exit__(self, *exc):
        start_database_service()


def test_first_backup():
    with DBHandler():
        run_offline_db_backup()


class db_status_handler(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database_service()
        return self

    def __exit__(self, *exc):
        start_database_service()


@db_status_handler()
def offline_db_backup():
    print("Running backup on database...")
    print("Backup finished")


"""
1.
Stopping database service
systemctl stop postgres
Running backup on database...
Backup finished
Starting database service
systemctl start postgres

2.
Stopping database service
systemctl stop postgres
Running backup on database...
Backup finished
Starting database service
systemctl start postgres
"""
