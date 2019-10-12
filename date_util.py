import calendar
import datetime

from enum import unique, IntEnum


@unique
class Order(IntEnum):
    FIRST = 0
    SECOND = 1
    THIRD = 2
    FOURTH = 3
    FIFTH = 4


def get_next_date_offset(day=calendar.MONDAY, date=datetime.datetime.now(), position=Order.FIRST):
    """
    Expects monday to be set to default calendar.MONDAY == 0

    :param day:
    :param date:
    :param position:
    :return:
    """

    month_range = calendar.monthrange(date.year, date.month)
    date_corrected = datetime.date(date.year, date.month, 1)
    month_range0 = month_range[0]
    offset = (day - month_range0)
    delta = (offset % 7) + (7 * position)

    new_date = date_corrected + datetime.timedelta(days=delta)
    if date.month == new_date.month:
        return new_date
    else:
        return None
