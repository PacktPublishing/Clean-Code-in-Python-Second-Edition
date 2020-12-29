""" Clean code in Python - Chapter 05, decorators

Unit tests for files `decorator_parametrized_*.py`
"""
import unittest
from unittest import mock
from typing import Optional, Type

from decorator_function_1 import (
    ControlledException,
    OperationObject,
    RunWithFailure,
)
from decorator_parametrized_1 import with_retry
from decorator_parametrized_2 import WithRetry


class WithRetryDecoratorTest(unittest.TestCase):
    decorators_to_test = (
        with_retry,
        WithRetry,
    )

    def setUp(self):
        self.info = mock.patch("log.logger.info").start()
        self.warning = mock.patch("log.logger.warning").start()

    def tearDown(self):
        self.info.stop()
        self.warning.stop()

    def _test_task_fails(
        self,
        fail_task_n_times: int,
        exception_cls: Type[Exception],
        expected_error_msg: Optional[str] = None,
        **deco_kwargs,
    ):
        for sut_deco in self.decorators_to_test:

            @sut_deco(**deco_kwargs)
            def test_run(task):
                return task.run()

            failing_task = RunWithFailure(
                OperationObject(),
                fail_n_times=fail_task_n_times,
                exception_cls=exception_cls,
            )
            with self.subTest(
                decorator_tested=sut_deco, decorated=test_run, **deco_kwargs
            ), self.assertRaises(exception_cls) as cm:
                test_run(failing_task)

            if expected_error_msg:
                self.assertEqual(str(cm.exception), expected_error_msg)

    def _test_task_calls_and_retries(
        self,
        fail_task_n_times: int,
        expected_times_run: int,
        expected_times_called: Optional[int] = None,
        exception_cls=ControlledException,
        **decorator_kwargs,
    ):
        """Generic test for the decorator under certain conditions
        Create a function, and apply each decorator to test, to it.
        Then verify the conditions hold with the values passed by parameter.
        """
        for sut_deco in self.decorators_to_test:

            @sut_deco(**decorator_kwargs)
            def test_run(task):
                return task.run()

            original_task = OperationObject()
            failing_task = RunWithFailure(
                original_task,
                fail_n_times=fail_task_n_times,
                exception_cls=exception_cls,
            )
            with self.subTest(
                decorator_tested=sut_deco,
                decorated=test_run,
                **decorator_kwargs,
            ):
                times_run = test_run(failing_task)

                self.assertEqual(times_run, expected_times_run)
                if expected_times_called:
                    self.assertEqual(
                        original_task._times_called, expected_times_called
                    )

    def test_fail_less_than_retry_limit(self):
        """failures = 2 < retries = 3 ==> must work"""
        self._test_task_calls_and_retries(
            fail_task_n_times=2,
            expected_times_run=3,
            expected_times_called=3,
        )

    def test_fail_equal_retry_limit(self):
        """Retry = fail = 3 ==> will fail"""
        self._test_task_fails(
            fail_task_n_times=3,
            exception_cls=RuntimeError,
        )

    def test_no_failures(self):
        """failures = 0, retries = 3 [default] ==> must work"""
        self._test_task_calls_and_retries(
            fail_task_n_times=0,
            expected_times_run=1,
            expected_times_called=1,
        )

    def test_retry_custom_limit_ok(self):
        """Retry = 5, fail = 2 ==> OK"""
        self._test_task_calls_and_retries(
            fail_task_n_times=2,
            expected_times_run=3,
            retries_limit=5,
        )

    def test_retry_custom_limit_fail(self):
        """Retry = 5, fail = 5, Fail"""
        self._test_task_fails(
            fail_task_n_times=5,
            exception_cls=RuntimeError,
            expected_error_msg="task failed 5 times",
            retries_limit=5,
            allowed_exceptions=(RuntimeError,),
        )

    def test_custom_exception_fails(self):
        """An unexpected (!= allowed) exception occurs ==> fail raising that exception."""
        for sut_deco in self.decorators_to_test:

            @sut_deco(allowed_exceptions=(AttributeError,))
            def test_run(task):
                return task.run()

            task = RunWithFailure(
                OperationObject(), fail_n_times=2, exception_cls=RuntimeError
            )
            with self.subTest(decorator_tested=sut_deco, decorated=test_run):
                with self.assertRaises(RuntimeError):
                    test_run(task)

    def test_custom_parameters_and_exception_fails(self):
        """doesn't catch the right exception, with retry limits != default."""
        for sut_deco in self.decorators_to_test:

            @sut_deco(
                retries_limit=4,
                allowed_exceptions=(ZeroDivisionError, AttributeError),
            )
            def test_run(task):
                return task.run()

            task = RunWithFailure(
                OperationObject(), fail_n_times=4, exception_cls=RuntimeError
            )
            with self.subTest(decorator_tested=sut_deco, decorated=test_run):
                with self.assertRaises(RuntimeError) as cm:
                    test_run(task)
                self.assertEqual(str(cm.exception), "task failed 1 times")

    def test_run_with_custom_parameters_controlled(self):
        """The exception raised, is one of the allowed ones for retry ==> retry."""
        self._test_task_calls_and_retries(
            fail_task_n_times=3,
            expected_times_run=4,
            retries_limit=4,
            exception_cls=AttributeError,
            allowed_exceptions=(ZeroDivisionError, AttributeError),
        )


if __name__ == "__main__":
    unittest.main()
