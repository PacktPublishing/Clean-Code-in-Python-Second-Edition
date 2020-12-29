import unittest
from contextlib import ContextDecorator
from unittest.mock import patch, DEFAULT

from contextmanagers import dbhandler_decorator, offline_backup, db_handler


class TestDBHandler(unittest.TestCase):
    def _patch_deps(self):
        return patch.multiple("contextmanagers", stop_database=DEFAULT, start_database=DEFAULT)

    def test_cm_calls_functions(self):
        with self._patch_deps() as deps:
            with dbhandler_decorator() as db_handler:
                handler_class = db_handler.__class__
                self.assertTrue(issubclass(handler_class, ContextDecorator), handler_class)

            deps["stop_database"].assert_called_once_with()
            deps["start_database"].assert_called_once_with()

    def test_cm_autocalled(self):
        with self._patch_deps() as deps:
            offline_backup()

            deps["stop_database"].assert_called_once_with()
            deps["start_database"].assert_called_once_with()

    def test_context_decorator_called_on_exception(self):
        """In case of an exception, the __exit__ is called anyways."""
        with self._patch_deps() as deps, patch("contextmanagers.run", side_effect=RuntimeError), self.assertRaises(
            RuntimeError
        ):
            offline_backup()

        deps["start_database"].assert_called_once_with()

    def test_db_handler_on_exception(self):
        with self._patch_deps() as deps, self.assertRaises(RuntimeError):
            with db_handler():
                raise RuntimeError("something went wrong!")

        deps["start_database"].assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
