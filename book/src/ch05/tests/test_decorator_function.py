import unittest
from unittest import mock
from functools import wraps

from decorator_function_1 import (
    retry,
    ControlledException,
    OperationObject,
    RunWithFailure,
)
from decorator_function_2 import Retry


@retry
def _run_op_1(task):
    """Test function using the function decorator."""
    return task.run()


@Retry
def _run_op_2(task):
    """Test function using the decorator defined as callable object."""
    return task.run()


TEST_CASES = (_run_op_1, _run_op_2)


def generate_test_cases(test_method):
    """Decorator to run <test_method> with all test functions as their input."""

    @wraps(test_method)
    def wrapped(self):
        for test_function in TEST_CASES:
            with self.subTest(test_function=test_function):
                test_method(self, test_function)

    return wrapped


class RetryDecoratorTest(unittest.TestCase):
    """Unit tests for the decorators in files 1 & 2
    (decorators as a function or callable objects, respectively).
    """

    def setUp(self):
        self.info = mock.patch("log.logger.info").start()

    def tearDown(self):
        self.info.stop()

    @generate_test_cases
    def test_fail_less_than_retry_limit(self, test_function):
        """Retry = 3, fail = 2, should work"""
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=2)
        times_run = test_function(failing_task)

        self.assertEqual(times_run, 3)
        self.assertEqual(task._times_called, 3)

    @generate_test_cases
    def test_fail_equal_retry_limit(self, test_function):
        """Retry = fail = 3, will fail"""
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=3)
        with self.assertRaises(ControlledException):
            test_function(failing_task)

    @generate_test_cases
    def test_no_failures(self, test_function):
        task = OperationObject()
        failing_task = RunWithFailure(task, fail_n_times=0)
        times_run = test_function(failing_task)

        self.assertEqual(times_run, 1)
        self.assertEqual(task._times_called, 1)

    def test_doc(self):
        for fx in TEST_CASES:
            with self.subTest(function=fx):
                self.assertTrue(fx.__doc__.startswith("Test function using"))


if __name__ == "__main__":
    unittest.main()
