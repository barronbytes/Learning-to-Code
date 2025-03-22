import unittest
from file_handler import FileHandler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.root_dir = FileHandler.root_dir()
    
    def test_root_dir(self):
        self.assertEqual(self.root_dir, ".")

    def test_get_data_files(self):
        expected_files = ['phase0.txt', 'phase2.txt', 'phase1.txt', 'phase3.txt']
        self.assertListEqual(FileHandler.get_data_files(self.root_dir), expected_files)


if __name__ == "__main__":
    unittest.main()