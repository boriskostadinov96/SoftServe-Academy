import unittest

from src.Task6 import converted_date


class TestConvertedDate(unittest.TestCase):

    def test_standard_cases(self):
        self.assertEqual(converted_date("12/31/2021"), "20213112")
        self.assertEqual(converted_date("01/01/2000"), "20000101")
        self.assertEqual(converted_date("11/15/1999"), "19991511")

    def test_single_digit_month_and_day(self):
        self.assertEqual(converted_date("3/4/2022"), "20220403")
        self.assertEqual(converted_date("5/9/1995"), "19950905")

    def test_leap_year_date(self):
        self.assertEqual(converted_date("02/29/2020"), "20202902")


if __name__ == "__main__":
    unittest.main()
