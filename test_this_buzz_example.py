import unittest
from this_buzz_example import buzz

class TestThisBuzz(unittest.TestCase):
    def test_buzz_divisible_by_3(self):
        self.assertEqual(buzz(3), 'Buzz!')
        self.assertEqual(buzz(6), 'Buzz!')
        self.assertEqual(buzz(9), 'Buzz!')

    def test_buzz_not_divisible_by_3(self):
        self.assertEqual(buzz(1), 1)
        self.assertEqual(buzz(4), 4)
        self.assertEqual(buzz(5), 5)

if __name__ == '__main__':
    unittest.main()
