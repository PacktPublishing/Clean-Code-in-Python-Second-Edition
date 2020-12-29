"""Clean code in Python - chapter 05

> PEP0614: Relaxing Grammar restrictions on decorators
https://www.python.org/dev/peps/pep-0614/
"""


def _log(f, *args, **kwargs):
    print(f"calling {f.__qualname__!r} with {args=} and {kwargs=}")
    return f(*args, **kwargs)


@(lambda f: lambda *args, **kwargs: _log(f, *args, **kwargs))
def func(x):
    return x + 1
