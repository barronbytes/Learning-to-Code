import unittest
import statistics as stats
from metrics import Metrics


class TestMetrics(unittest.TestCase):
    
    def test_average(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        avg = stats.mean(data)
        self.assertEqual(Metrics().average(data), round(avg, 2))


if __name__ == "__main__":
    unittest.main()