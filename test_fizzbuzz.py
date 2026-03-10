import unittest
from fizzbuzz import fizzbuzz, fizzbuzz_list

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_neither(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_fizzbuzz_list_length(self):
        result = fizzbuzz_list()
        self.assertEqual(len(result), 100)

    def test_fizzbuzz_list_content(self):
        result = fizzbuzz_list()
        self.assertEqual(result[0], "1")
        self.assertEqual(result[2], "Fizz")  # 3rd element
        self.assertEqual(result[4], "Buzz")  # 5th element
        self.assertEqual(result[14], "FizzBuzz")  # 15th element

if __name__ == '__main__':
    unittest.main()
