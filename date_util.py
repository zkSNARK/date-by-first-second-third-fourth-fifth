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

def get_next_date_offset(day = calendar.MONDAY, date = datetime.datetime.now(), position = Order.FIRST):
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
    return date_corrected + datetime.timedelta(days=delta)



if __name__ == "__main__":
    first_mondays_2019 = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2]
    second_mondays_2019 = [14, 11, 11, 8, 13, 10, 8, 12, 9, 14, 11, 9]
    third_mondays_2019 = [21, 18, 18, 15, 20, 17, 15, 19, 16, 21, 18, 16]
    third_mondays_2019 = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2]
    fourth_mondays_2019 = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2]

    first_tuesdays_2019 = [1, 5, 5, 2, 7, 4, 2, 6, 3, 1, 5, 3]
    first_mondays_2020 = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2]

    # for i in range(1, 13):
    #     seed_date = datetime.date(year=2019, month=i, day=1)
    #     date_of_first_mon = get_next_date_offset(date=seed_date)
    #     print(date_of_first_mon.day)
    #     d1 = first_mondays_2019[i - 1]
    #     d2 = date_of_first_mon.day
    #     assert (d1 == d2)

    for i in range(1, 13):
        seed_date = datetime.date(year=2019, month=i, day=1)
        date_of_second_mon = get_next_date_offset(date=seed_date, position=Order.SECOND)
        print(date_of_second_mon.day)
        d1 = second_mondays_2019[i - 1]
        d2 = date_of_second_mon.day
        assert (d1 == d2)

    # for i in range(1, 13):
    #     seed_date = datetime.date(year=2019, month=i, day=1)
    #     date_of_first_tues = get_next_date_offset(day=calendar.TUESDAY, date=seed_date)
    #     print(date_of_first_tues.day)
    #     d1 = first_tuesdays_2019[i - 1]
    #     d2 = date_of_first_tues.day
    #     assert (d1 == d2)
