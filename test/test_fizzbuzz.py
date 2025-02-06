
import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        test_cases = [
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (5, "Buzz"),
            (6, "Fizz"),
            (10, "Buzz"),
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
            (45, "FizzBuzz"),
            (7, "7"),
            (8, "8"),
            (78, "Fizz"),
            (12, "Fizz"),
            (20, "Buzz"),
            (25, "Buzz"),
            (50, "Buzz"),
            (90, "FizzBuzz"),
        ]

        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fizzbuzz(n), expected)


if __name__ == "__main__":
    unittest.main()