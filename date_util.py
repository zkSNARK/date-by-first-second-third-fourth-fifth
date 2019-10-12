import calendar
import datetime

from enum import unique, IntEnum
from typing import Optional


@unique
class Ordinal(IntEnum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    FIFTH = 4


def get_next_date_offset(day=calendar.MONDAY, date=datetime.datetime.now(), ordinal=Ordinal.FIRST) -> Optional[datetime.date]:
    """Get the date of a day of the week specified by an ordinal value (or int).

    Expects monday to be set to default calendar.MONDAY == 0

    :param day: The calendar day from library calendar enum.
    :param date: The date or datetime which is in the month you want to target.
        Any date in a particular month will work here.
    :param ordinal: This is the ordinal ordering, pass one of the ordinals from
        the enum provided above.
    :return: date or None
    """

    month_range = calendar.monthrange(date.year, date.month)
    date_corrected = datetime.date(date.year, date.month, 1)
    month_range0 = month_range[0]
    offset = (day - month_range0)
    delta = (offset % 7) + (7 * ordinal)

    new_date = date_corrected + datetime.timedelta(days=delta)
    if date.month == new_date.month:
        return new_date
    else:
        return None
