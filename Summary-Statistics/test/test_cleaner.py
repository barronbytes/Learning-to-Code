import unittest
from cleaner import Cleaner

class TestCleaner(unittest.TestCase):

    def test_is_list(self):
        data = []
        self.assertTrue(Cleaner(data).is_list())

    def test_data_not_list(self):
        data = "Hello World"
        self.assertEqual(Cleaner(data).brain(), None)

    def test_data_list_empty(self):
        data = []
        self.assertEqual(Cleaner(data).brain(), None)

    def test_data_list_letters(self):
        data = ["  Hello  ", "  World  \n"]
        self.assertEqual(Cleaner(data).brain(), None)

if __name__ == "__main__":
    unittest.main()