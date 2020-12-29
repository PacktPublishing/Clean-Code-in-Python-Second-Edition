"""Tests for async_context_manager"""

import unittest
from unittest.mock import DEFAULT, patch

from async_context_manager import db_management, run_db_backup


class TestAsyncContextManager(unittest.IsolatedAsyncioTestCase):
    def _patch_deps(self):
        return patch.multiple(
            "async_context_manager",
            stop_database=DEFAULT,
            start_database=DEFAULT,
            create_metrics_logger=DEFAULT,
        )

    async def test_db_handler_on_exception(self):
        with self._patch_deps() as deps, self.assertRaises(RuntimeError):
            async with db_management():
                raise RuntimeError("something went wrong!")

        deps["start_database"].assert_called_once_with()

    async def test_cm_autocalled(self):
        with self._patch_deps() as deps:
            await run_db_backup()

            deps["stop_database"].assert_called_once_with()
            deps["start_database"].assert_called_once_with()
            deps["create_metrics_logger"].assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
