import calendar
import datetime
from unittest import TestCase

from date_util import get_next_date_offset, Ordinal


class GetMondayDateOffset(TestCase):
    first_mondays_2019 = [7, 4, 4, 1, 6, 3, 1, 5, 2, 7, 4, 2]
    second_mondays_2019 = [14, 11, 11, 8, 13, 10, 8, 12, 9, 14, 11, 9]
    third_mondays_2019 = [21, 18, 18, 15, 20, 17, 15, 19, 16, 21, 18, 16]
    fourth_mondays_2019 = [28, 25, 25, 22, 27, 24, 22, 26, 23, 28, 25, 23]
    fifth_mondays_2019 = [None, None, None, 29, None, None, 29, None, 30, None, None, 30]

    first_mondays_2020 = [6, 3, 2, 6, 4, 1, 6, 3, 7, 5, 2, 7]
    second_mondays_2020 = [13, 10, 9, 13, 11, 8, 13, 10, 14, 12, 9, 14]
    third_mondays_2020 = [20, 17, 16, 20, 18, 15, 20, 17, 21, 19, 16, 21]
    fourth_mondays_2020 = [27, 24, 23, 27, 25, 22, 27, 24, 28, 26, 23, 28]
    fifth_mondays_2020 = [None, None, 30, None, None, 29, None, 31, None, None, 30, None]

    first_mondays_2021 = [4, 1, 1, 5, 3, 7, 5, 2, 6, 4, 1, 6]
    second_mondays_2021 = [11, 8, 8, 12, 10, 14, 12, 9, 13, 11, 8, 13]
    third_mondays_2021 = [18, 15, 15, 19, 17, 21, 19, 16, 20, 18, 15, 20]
    fourth_mondays_2021 = [25, 22, 22, 26, 24, 28, 26, 23, 27, 25, 22, 27]
    fifth_mondays_2021 = [None, None, 29, None, 31, None, None, 30, None, None, 29, None]

    first_mondays_2022 = [3, 7, 7, 4, 2, 6, 4, 1, 5, 3, 7, 5]
    second_mondays_2022 = [10, 14, 14, 11, 9, 13, 11, 8, 12, 10, 14, 12]
    third_mondays_2022 = [17, 21, 21, 18, 16, 20, 18, 15, 19, 17, 21, 19]
    fourth_mondays_2022 = [24, 28, 28, 25, 23, 27, 25, 22, 26, 24, 28, 26]
    fifth_mondays_2022 = [31, None, None, None, 30, None, None, 29, None, 31, None, None]

    def test_first_mondays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_mondays_2019[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_mondays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_mondays_2019[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_mondays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_mondays_2019[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_mondays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_mondays_2019[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_mondays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_mondays_2019[i - 1], d2)

    def test_first_mondays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_mondays_2020[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_mondays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_mondays_2020[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_mondays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_mondays_2020[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_mondays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_mondays_2020[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_mondays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_mondays_2020[i - 1], d2)

    def test_first_mondays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_mondays_2021[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_mondays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_mondays_2021[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_mondays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_mondays_2021[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_mondays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_mondays_2021[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_mondays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_mondays_2021[i - 1], d2)

    def test_first_mondays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_mondays_2022[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_mondays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_mondays_2022[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_mondays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_mondays_2022[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_mondays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_mondays_2022[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_mondays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            d2 = self.fifth_mondays_2022[i - 1]
            d1 = get_next_date_offset(day=calendar.MONDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d1:
                d1 = d1.day
            self.assertEqual(d1, d2)

