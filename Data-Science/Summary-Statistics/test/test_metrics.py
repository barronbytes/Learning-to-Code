import unittest
import statistics as stats
from metrics import Metrics


class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7]

    def test_average(self):
        avg = stats.mean(self.data)
        self.assertEqual(Metrics().average(self.data), round(avg, 2))

    def test_maximum(self):
        pass

if __name__ == "__main__":
    unittest.main()