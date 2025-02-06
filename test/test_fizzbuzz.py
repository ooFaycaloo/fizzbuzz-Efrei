import unittest
from io import StringIO
import sys
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        # Capture la sortie standard
        captured_output = StringIO()
        sys.stdout = captured_output

        # Exécute la fonction
        fizzbuzz(15)

        # Récupère la sortie
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().splitlines()

        # Vérifie les résultats attendus
        expected_output = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()