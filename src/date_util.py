import calendar
import datetime

from typing import Optional


def get_date_of(ordinal=None, day=None, month=None, year=None, date=None) -> Optional[datetime.date]:
    """Get the date of a day of the week specified by an ordinal value (or int).

    As an example, you can read the API of this utility as follows.

        data = get_date_of ( the first monday in January of 2021)

    Expects monday to be set to the calendar library default firstweekday == 0.
    Check your first day by calling calendar.firstweekday().  See...
        https://docs.python.org/3/library/calendar.html#calendar.firstweekday


    :param ordinal: This is the ordinal ordering, pass one of the ordinals from
        the Ordinal enum found in ordinal.py
    :param day: The calendar day from calendar library.
    :param date: The date or datetime which is in the month you want to target.
        Any date in a particular month will work here.
        NOTE: you should either pass this, or you should pass the two following
              parameters (month, year)
    :param month: if you didn't pass the date, pass the month as an int
    :param year: if you didn't pass the date, pass the month as an int


    :return: date or None if the request doesn't exist in the given month / year
    """

    if month is not None and year is not None:
        date = datetime.date(year=year, month=month, day=1)

    month_range = calendar.monthrange(date.year, date.month)
    first_of_month = datetime.date(date.year, date.month, 1)
    month_range0 = month_range[0]
    offset = (day - month_range0)
    delta = (offset % 7) + (7 * (ordinal - 1))

    new_date = first_of_month + datetime.timedelta(days=delta)
    if date.month == new_date.month:
        return new_date
    else:
        return None
