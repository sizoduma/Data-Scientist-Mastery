import unittest
import pandas as pd
from datetime import datetime
from src.features import compute_rfm_features


class TestFeatures(unittest.TestCase):
    
    def setUp(self):
        self.transactions = pd.DataFrame({
            'customer_id': [1, 1, 2, 2, 3],
            'date': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-01-15', '2024-02-15', '2024-02-20']),
            'amount': [100, 150, 200, 250, 300],
            'transaction_id': range(1, 6),
        })
    
    def test_rfm_features(self):
        reference_date = datetime(2024, 3, 1)
        rfm = compute_rfm_features(self.transactions, reference_date)
        
        # Check that all customers are present
        self.assertEqual(len(rfm), 3)
        
        # Check that Frequency is correct
        self.assertEqual(rfm.loc[1, 'frequency'], 2)
        self.assertEqual(rfm.loc[2, 'frequency'], 2)
        self.assertEqual(rfm.loc[3, 'frequency'], 1)


if __name__ == '__main__':
    unittest.main()
