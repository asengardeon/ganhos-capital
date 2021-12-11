import os
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = os.system("python ../source/main.py")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
