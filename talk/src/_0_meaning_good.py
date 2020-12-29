"""
This time, the function is rewritten, naming its parts,
so it is clear what is doing at each stage
"""


def is_leap(year):
    return year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)


def number_of_days(year):
    return 366 if is_leap(year) else 365


def elapse(year):
    days = number_of_days(year)
    for day in range(1, days + 1):
        print("Day {} of {}".format(day, year))
