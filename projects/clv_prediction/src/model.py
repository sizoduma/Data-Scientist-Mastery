from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, precision_recall_curve
import pandas as pd
import numpy as np


def train_model(X_train, y_train, algorithm='gb', params=None):
    """
    Train a machine learning model.
    """
    if params is None:
        params = {}
    
    if algorithm == 'linear':
        model = LinearRegression()
    elif algorithm == 'gb':
        model = GradientBoostingRegressor(
            n_estimators=params.get('n_estimators', 100),
            max_depth=params.get('max_depth', 5),
            learning_rate=params.get('learning_rate', 0.1),
            random_state=42
        )
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    """
    y_pred = model.predict(X_test)
    
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    
    metrics = {
        'rmse': rmse,
        'mae': mae,
        'predictions': y_pred,
    }
    return metrics


def compute_business_metrics(y_true, y_pred, percentile=20):
    """
    Compute business-aligned metrics.
    E.g., lift: do top 20% of predictions capture 50%+ of true high-value customers?
    """
    df_eval = pd.DataFrame({'true': y_true, 'pred': y_pred})
    df_eval = df_eval.sort_values('pred', ascending=False)
    
    top_k_pct = int(len(df_eval) * percentile / 100)
    top_k_true_sum = df_eval.head(top_k_pct)['true'].sum()
    total_true_sum = df_eval['true'].sum()
    
    capture_rate = top_k_true_sum / total_true_sum if total_true_sum > 0 else 0
    
    return {
        'capture_rate_top_k': capture_rate,
        'target_met': capture_rate >= 0.5,  # Target: top 20% captures 50%+
    }


if __name__ == "__main__":
    print("Model training module ready.")
