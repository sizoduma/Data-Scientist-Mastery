import pandas as pd
import numpy as np
from typing import Tuple


def load_customer_data(path: str) -> pd.DataFrame:
    """
    Load customer dimension table.
    Expected columns: customer_id, signup_date, country, segment
    """
    df = pd.read_csv(path)
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    return df


def load_transaction_data(path: str) -> pd.DataFrame:
    """
    Load transaction fact table.
    Expected columns: transaction_id, customer_id, date, amount, category
    """
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df


def validate_data_schema(df: pd.DataFrame, required_cols: list) -> bool:
    """
    Check that data contains required columns.
    """
    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return True


def check_data_quality(transactions: pd.DataFrame) -> dict:
    """
    Assess data quality and return summary.
    """
    report = {
        'total_records': len(transactions),
        'missing_values': transactions.isnull().sum().to_dict(),
        'date_range': (transactions['date'].min(), transactions['date'].max()),
        'unique_customers': transactions['customer_id'].nunique(),
        'duplicate_records': transactions.duplicated().sum(),
    }
    return report


if __name__ == "__main__":
    # Example usage
    print("Data loading module ready.")
