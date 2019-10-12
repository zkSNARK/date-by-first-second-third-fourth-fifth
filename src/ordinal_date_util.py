import calendar
import datetime

from typing import Optional

from enum import IntEnum, unique


@unique
class month(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


@unique
class ordinal(IntEnum):
    ZEROITH = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    NINTH = 9
    TENTH = 10
    ELEVENTH = 11
    TWELFTH = 12
    THIRTEENTH = 13
    FOURTEENTH = 14
    FIFTEENTH = 15
    SIXTEENTH = 16
    SEVENTEENTH = 17
    EIGHTEENTH = 18
    NINETEENTH = 19
    TWENTIETH = 20
    TWENTYFIRST = 21
    TWENTYSECOND = 22
    TWENTYTHIRD = 23
    TWENTYFOURTH = 24
    TWENTYFIFTH = 25
    TWENTYSIXTH = 26
    TWENTYSEVENTH = 27
    TWENTYEIGHTH = 28
    TWENTYNINTH = 29
    THIRTIETH = 30
    THIRTYFIRST = 31
    THIRTYSECOND = 32
    THIRTYTHIRD = 33
    THIRTYFOURTH = 34
    THIRTYFIFTH = 35
    THIRTYSIXTH = 36
    THIRTYSEVENTH = 37
    THIRTYEIGHTH = 38
    THIRTYNINTH = 39
    FORTIETH = 40
    FORTYFIRST = 41
    FORTYSECOND = 42
    FORTYTHIRD = 43
    FORTYFOURTH = 44
    FORTYFIFTH = 45
    FORTYSIXTH = 46
    FORTYSEVENTH = 47
    FORTYEIGHTH = 48
    FORTYNINTH = 49
    FIFTIETH = 50
    FIFTYFIRST = 51
    FIFTYSECOND = 52
    FIFTYTHIRD = 53
    FIFTYFOURTH = 54
    FIFTYFIFTH = 55
    FIFTYSIXTH = 56
    FIFTYSEVENTH = 57
    FIFTYEIGHTH = 58
    FIFTYNINTH = 59
    SIXTIETH = 60
    SIXTYFIRST = 61
    SIXTYSECOND = 62
    SIXTYTHIRD = 63
    SIXTYFOURTH = 64
    SIXTYFIFTH = 65
    SIXTYSIXTH = 66
    SIXTYSEVENTH = 67
    SIXTYEIGHTH = 68
    SIXTYNINTH = 69
    SEVENTIETH = 70
    SEVENTYFIRST = 71
    SEVENTYSECOND = 72
    SEVENTYTHIRD = 73
    SEVENTYFOURTH = 74
    SEVENTYFIFTH = 75
    SEVENTYSIXTH = 76
    SEVENTYSEVENTH = 77
    SEVENTYEIGHTH = 78
    SEVENTYNINTH = 79
    EIGHTIETH = 80
    EIGHTYFIRST = 81
    EIGHTYSECOND = 82
    EIGHTYTHIRD = 83
    EIGHTYFOURTH = 84
    EIGHTYFIFTH = 85
    EIGHTYSIXTH = 86
    EIGHTYSEVENTH = 87
    EIGHTYEIGHTH = 88
    EIGHTYNINTH = 89
    NINETIETH = 90
    NINETYFIRST = 91
    NINETYSECOND = 92
    NINETYTHIRD = 93
    NINETYFOURTH = 94
    NINETYFIFTH = 95
    NINETYSIXTH = 96
    NINETYSEVENTH = 97
    NINETYEIGHTH = 98
    NINETYNINTH = 99
    HUNDREDETH = 100


def get_date_of(ordinal=None, day=None, month=None, year=None, date=None) -> Optional[datetime.date]:
    """Get the date of a day of the week specified by an ordinal value (or int).

    As an example, you can read the API of this utility as follows.

        data = get_date_of ( the first monday in January of 2021)

    Expects monday to be set to the calendar library default firstweekday == 0.
    Check your first day by calling calendar.firstweekday().  See...
        https://docs.python.org/3/library/calendar.html#calendar.firstweekday


    :param ordinal: This is the ordinal ordering, pass one of the ordinals from
        the ordinal enum above
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
