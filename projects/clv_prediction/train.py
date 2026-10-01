# Training script for CLV prediction model

import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.data import load_customer_data, load_transaction_data, check_data_quality
from src.features import engineer_features
from src.model import train_model, evaluate_model, compute_business_metrics
from src.utils import setup_logging, save_metrics, load_config


def main():
    logger = setup_logging()
    logger.info("Starting CLV prediction training pipeline.")
    
    # Load config
    config = load_config('config/params.yaml')
    
    # Load data
    logger.info("Loading data...")
    customers = load_customer_data(config['data']['raw_path'] + 'customers.csv')
    transactions = load_transaction_data(config['data']['raw_path'] + 'transactions.csv')
    
    # Validate and assess quality
    logger.info("Validating data quality...")
    quality_report = check_data_quality(transactions)
    logger.info(f"Data quality report: {quality_report}")
    
    # Engineer features
    logger.info("Engineering features...")
    features_df = engineer_features(customers, transactions)
    
    # Define target: high CLV = top quartile of monetary spend
    features_df['clv_target'] = (features_df['monetary'] > features_df['monetary'].quantile(0.75)).astype(int)
    
    # Prepare train/test split
    X = features_df.drop(['customer_id', 'clv_target', 'signup_date'], axis=1, errors='ignore')
    y = features_df['clv_target']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=1 - config['data']['train_split'],
        random_state=config['data']['random_state'],
        stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    logger.info("Training model...")
    model = train_model(X_train_scaled, y_train, algorithm='gb', params=config['model']['hyperparams'])
    
    # Evaluate
    logger.info("Evaluating model...")
    metrics = evaluate_model(model, X_test_scaled, y_test)
    business_metrics = compute_business_metrics(y_test, metrics['predictions'])
    
    logger.info(f"RMSE: {metrics['rmse']:.4f}")
    logger.info(f"Business metric (top 20% capture rate): {business_metrics['capture_rate_top_k']:.2%}")
    logger.info(f"Target met: {business_metrics['target_met']}")
    
    # Save results
    save_metrics({
        'rmse': metrics['rmse'],
        'mae': metrics['mae'],
        'capture_rate': business_metrics['capture_rate_top_k'],
        'target_met': business_metrics['target_met'],
    }, 'results/metrics/latest.json')
    
    logger.info("Training pipeline complete.")


if __name__ == '__main__':
    main()
