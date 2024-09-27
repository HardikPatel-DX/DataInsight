import unittest
import pandas as pd
from src.data_analysis import summary_statistics

class TestSummaryStatistics(unittest.TestCase):
    
    def test_summary_statistics(self):
        data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
        df = pd.DataFrame(data)
        summary = summary_statistics(df)
        self.assertEqual(summary.loc['mean', 'A'], 3)
        self.assertEqual(summary.loc['mean', 'B'], 3)

if __name__ == '__main__':
    unittest.main()
