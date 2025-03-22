import unittest
import statistics as stats
from metrics import Metrics


class TestMetrics(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5, 6, 7]

    def test_average(self):
        avg = stats.mean(self.data)
        mu = round(avg, 2)
        self.assertEqual(Metrics().average(self.data), mu)

    def test_maximum(self):
        max_num = max(self.data)
        self.assertEqual(Metrics().maximum(self.data), max_num)

    def test_variance(self):
        variance = stats.pvariance(self.data)
        sigma = round(variance, 2)
        self.assertEqual(Metrics().variance(self.data), sigma)


if __name__ == "__main__":
    unittest.main()