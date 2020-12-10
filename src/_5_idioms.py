"""
This section collects other common idioms in Python for performing
general tasks in a more efficient way.

The code is for explanatory purposes only.
"""

DATA_FILE = '/tmp/file.txt'


def count_words_1(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


def count_words_2(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count


def count_words_3(words):
    from collections import Counter
    count = Counter(words)
    return count


def ignore_exceptions_1():
    data = None
    try:
        with open(DATA_FILE) as f:
            data = f.read()
    except (FileNotFoundError, PermissionError):
        pass
    return data


def ignore_exceptions_2():
    data = None
    import contextlib
    with contextlib.suppress(FileNotFoundError, PermissionError):
        with open(DATA_FILE) as f:
            data = f.read()
    return data


def find_first_even_1(*numbers):
    for number in numbers:
        if number % 2 == 0:
            return number


def find_first_even_2(*numbers):
    try:
        return [number for number in numbers if number % 2 == 0][0]
    except IndexError:
        pass


def find_first_even_3(*numbers):
    return next((number for number in numbers if number % 2 == 0), None)
