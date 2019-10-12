import calendar
import datetime
from unittest import TestCase

from src.date_util import get_next_date_offset, Ordinal


class GetTuesdayDateOffset(TestCase):
    first_tuesdays_2019 = [1, 5, 5, 2, 7, 4, 2, 6, 3, 1, 5, 3]
    second_tuesdays_2019 = [8, 12, 12, 9, 14, 11, 9, 13, 10, 8, 12, 10]
    third_tuesdays_2019 = [15, 19, 19, 16, 21, 18, 16, 20, 17, 15, 19, 17]
    fourth_tuesdays_2019 = [22, 26, 26, 23, 28, 25, 23, 27, 24, 22, 26, 24]
    fifth_tuesdays_2019 = [29, None, None, 30, None, None, 30, None, None, 29, None, 31]

    first_tuesdays_2020 = [7, 4, 3, 7, 5, 2, 7, 4, 1, 6, 3, 1]
    second_tuesdays_2020 = [14, 11, 10, 14, 12, 9, 14, 11, 8, 13, 10, 8]
    third_tuesdays_2020 = [21, 18, 17, 21, 19, 16, 21, 18, 15, 20, 17, 15]
    fourth_tuesdays_2020 = [28, 25, 24, 28, 26, 23, 28, 25, 22, 27, 24, 22]
    fifth_tuesdays_2020 = [None, None, 31, None, None, 30, None, None, 29, None, None, 29]

    first_tuesdays_2021 = [5, 2, 2, 6, 4, 1, 6, 3, 7, 5, 2, 7]
    second_tuesdays_2021 = [12, 9, 9, 13, 11, 8, 13, 10, 14, 12, 9, 14]
    third_tuesdays_2021 = [19, 16, 16, 20, 18, 15, 20, 17, 21, 19, 16, 21]
    fourth_tuesdays_2021 = [26, 23, 23, 27, 25, 22, 27, 24, 28, 26, 23, 28]
    fifth_tuesdays_2021 = [None, None, 30, None, None, 29, None, 31, None, None, 30, None]

    first_tuesdays_2022 = [4, 1, 1, 5, 3, 7, 5, 2, 6, 4, 1, 6]
    second_tuesdays_2022 = [11, 8, 8, 12, 10, 14, 12, 9, 13, 11, 8, 13]
    third_tuesdays_2022 = [18, 15, 15, 19, 17, 21, 19, 16, 20, 18, 15, 20]
    fourth_tuesdays_2022 = [25, 22, 22, 26, 24, 28, 26, 23, 27, 25, 22, 27]
    fifth_tuesdays_2022 = [None, None, 29, None, 31, None, None, 30, None, None, 29, None]

    def test_first_tuesdays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_tuesdays_2019[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_tuesdays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_tuesdays_2019[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_tuesdays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_tuesdays_2019[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_tuesdays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_tuesdays_2019[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_tuesdays_2019(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2019, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_tuesdays_2019[i - 1], d2)

    def test_first_tuesdays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_tuesdays_2020[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_tuesdays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_tuesdays_2020[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_tuesdays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_tuesdays_2020[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_tuesdays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_tuesdays_2020[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_tuesdays_2020(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2020, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_tuesdays_2020[i - 1], d2)

    def test_first_tuesdays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_tuesdays_2021[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_tuesdays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_tuesdays_2021[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_tuesdays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_tuesdays_2021[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_tuesdays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_tuesdays_2021[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_tuesdays_2021(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2021, month=i, day=1)
            d2 = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d2:
                d2 = d2.day
            self.assertEqual(self.fifth_tuesdays_2021[i - 1], d2)

    def test_first_tuesdays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_first_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIRST)
            d2 = self.first_tuesdays_2022[i - 1]
            d1 = date_of_first_mon.day
            self.assertEqual(d1, d2)

    def test_second_tuesdays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_second_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.SECOND)
            d2 = self.second_tuesdays_2022[i - 1]
            d1 = date_of_second_mon.day
            self.assertEqual(d1, d2)

    def test_third_tuesdays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_third_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.THIRD)
            d2 = self.third_tuesdays_2022[i - 1]
            d1 = date_of_third_mon.day
            self.assertEqual(d1, d2)

    def test_fourth_tuesdays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            date_of_fourth_mon = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FOURTH)
            d2 = self.fourth_tuesdays_2022[i - 1]
            d1 = date_of_fourth_mon.day
            self.assertEqual(d1, d2)

    def test_fifth_tuesdays_2022(self):
        for i in range(1, 13):
            seed_date = datetime.date(year=2022, month=i, day=1)
            d2 = self.fifth_tuesdays_2022[i - 1]
            d1 = get_next_date_offset(day=calendar.TUESDAY, date=seed_date, ordinal=Ordinal.FIFTH)
            if d1:
                d1 = d1.day
            self.assertEqual(d1, d2)
