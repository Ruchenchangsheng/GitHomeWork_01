from app import add
import unittest

class add_test(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(add(2, 2), 4)


if __name__ == '__main__':
    unittest.main()