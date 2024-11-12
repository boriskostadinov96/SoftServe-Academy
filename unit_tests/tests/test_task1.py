import unittest
from src.Task1 import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_3(self):
        self.assertEqual(FizzBuzz(3), "Fizz")
        self.assertEqual(FizzBuzz(9), "Fizz")

    def test_multiple_of_5(self):
        self.assertEqual(FizzBuzz(5), "Buzz")
        self.assertEqual(FizzBuzz(10), "Buzz")

    def test_multiple_of_3_and_5(self):
        self.assertEqual(FizzBuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz(30), "FizzBuzz")

    def test_not_multiple_of_3_or_5(self):
        self.assertEqual(FizzBuzz(1), "1")
        self.assertEqual(FizzBuzz(7), "7")
        self.assertEqual(FizzBuzz(13), "13")


if __name__ == "__main__":
    unittest.main()

