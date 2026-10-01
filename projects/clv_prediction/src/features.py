import pandas as pd
import numpy as np
from datetime import datetime


def compute_rfm_features(transactions: pd.DataFrame, reference_date: datetime) -> pd.DataFrame:
    """
    Compute Recency, Frequency, Monetary features per customer.
    
    Recency: days since last purchase
    Frequency: number of purchases
    Monetary: total spend
    """
    customer_rfm = transactions.groupby('customer_id').agg({
        'date': lambda x: (reference_date - x.max()).days,
        'transaction_id': 'count',
        'amount': 'sum',
    }).rename(columns={
        'date': 'recency_days',
        'transaction_id': 'frequency',
        'amount': 'monetary'
    })
    return customer_rfm


def compute_temporal_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Compute time-based features.
    E.g., average days between purchases, trend in spending.
    """
    customer_temporal = transactions.sort_values('date').groupby('customer_id').agg({
        'date': ['min', 'max', 'nunique'],
        'amount': ['mean', 'std', 'min', 'max'],
    })
    customer_temporal.columns = [
        'first_purchase_date', 'last_purchase_date', 'purchase_count',
        'avg_transaction_amount', 'std_transaction_amount',
        'min_transaction_amount', 'max_transaction_amount'
    ]
    customer_temporal['customer_lifetime_days'] = (
        customer_temporal['last_purchase_date'] - customer_temporal['first_purchase_date']
    ).dt.days
    return customer_temporal


def compute_behavioral_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Compute behavioral features like category diversity, purchase timing.
    """
    customer_behavior = transactions.groupby('customer_id').agg({
        'category': 'nunique',  # Product category diversity
        'amount': lambda x: (x > x.quantile(0.75)).sum(),  # High-value purchases
    }).rename(columns={
        'category': 'category_diversity',
        'amount': 'high_value_purchase_count'
    })
    return customer_behavior


def engineer_features(customers: pd.DataFrame, transactions: pd.DataFrame, reference_date: datetime = None) -> pd.DataFrame:
    """
    Orchestrate feature engineering pipeline.
    """
    if reference_date is None:
        reference_date = transactions['date'].max()
    
    rfm = compute_rfm_features(transactions, reference_date)
    temporal = compute_temporal_features(transactions)
    behavioral = compute_behavioral_features(transactions)
    
    features = customers.set_index('customer_id').join([rfm, temporal, behavioral])
    features = features.fillna(0)
    return features.reset_index()


if __name__ == "__main__":
    print("Feature engineering module ready.")
