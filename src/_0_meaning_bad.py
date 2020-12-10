"""
Examples of code logic with no aparent meaning assigned,
making it hard to figure out the intention of the code.
"""


def elapse(year):
    days = 365
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        days += 1
    for day in range(1, days + 1):
        print("Day {} of {}".format(day, year))
