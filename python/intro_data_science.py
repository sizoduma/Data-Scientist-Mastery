import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def load_and_preview(csv_path: str):
    df = pd.read_csv(csv_path)
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print(df.head())
    return df


def summarize_numeric(df: pd.DataFrame):
    return df.describe().T


def clean_missing_values(df: pd.DataFrame):
    df_clean = df.copy()
    for col in df_clean.columns:
        if df_clean[col].dtype.kind in "if":
            df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        else:
            df_clean[col] = df_clean[col].fillna(df_clean[col].mode().iloc[0])
    return df_clean


if __name__ == "__main__":
    sample_df = pd.DataFrame({
        "age": [25, 30, 35, None, 40, 55],
        "income": [40000, 50000, 60000, 80000, None, 90000],
        "segment": ["A", "B", "A", "C", "B", "A"],
    })

    print("Summary before cleaning:")
    print(sample_df)
    print("\nNumeric summary:\n")
    print(summarize_numeric(sample_df))

    cleaned = clean_missing_values(sample_df)
    print("\nAfter cleaning:\n")
    print(cleaned)

    plt.hist(cleaned["age"], bins=10)
    plt.title("Age distribution")
    plt.show()
