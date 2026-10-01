# Project: Customer Lifetime Value Prediction

## Overview
This project demonstrates a production-ready machine learning workflow for predicting which customers have high lifetime value (CLV). The project includes data exploration, feature engineering, model training, and business impact evaluation.

## Dataset requirements
You'll need:
1. **Customers table**: customer_id, signup_date, country, segment
2. **Transactions table**: transaction_id, customer_id, date, amount, category

## Getting started

```bash
cd projects/clv_prediction
pip install -r requirements.txt

# Run training
python train.py

# Run tests
pytest tests/
```

## Key files
- `notebooks/01_exploration.ipynb` — Data exploration and visualization
- `notebooks/02_preprocessing.ipynb` — Data cleaning and transformation
- `notebooks/03_modeling.ipynb` — Model training and evaluation
- `src/` — Production-ready modules for data, features, and modeling
- `train.py` — End-to-end training pipeline

## Evaluation
The model is evaluated on:
1. **Statistical metrics**: RMSE, MAE
2. **Business metrics**: Do the top 20% of predictions capture 50%+ of high-CLV customers?

## Next steps
1. Add cross-validation
2. Implement hyperparameter tuning
3. Add model explainability (SHAP)
4. Build inference API
5. Set up monitoring for production
