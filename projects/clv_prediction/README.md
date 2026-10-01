# Advanced ML Project Template

This is a production-ready project structure for end-to-end machine learning work.

## Project: Customer Lifetime Value (CLV) Prediction

A realistic consulting project that demonstrates:
- Data exploration and quality assessment
- Feature engineering at scale
- Model selection and hyperparameter tuning
- Business-aligned evaluation and interpretation
- Reproducibility and collaboration

## Directory structure

```
clv_prediction/
├── README.md                 # Project overview and business context
├── requirements.txt          # Python dependencies
├── config/
│   └── params.yaml          # Experiment hyperparameters
├── data/
│   ├── raw/                 # Original, immutable data
│   ├── processed/           # Cleaned and transformed data
│   └── metadata/            # Schema and data dictionaries
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data.py              # Loading and validation
│   ├── features.py          # Feature engineering
│   ├── model.py             # Training and evaluation
│   └── utils.py             # Helpers and logging
├── tests/
│   ├── test_features.py
│   ├── test_model.py
│   └── test_data.py
├── results/
│   ├── models/              # Trained model artifacts
│   ├── metrics/             # Performance logs
│   └── plots/               # Visualizations
└── train.py                 # Entry point for training
```

## Business context

**Goal**: Predict which customers have high lifetime value (CLV) to prioritize retention efforts.

**Success metric**: Top 20% of predicted high-CLV customers should include 50%+ of actual high-CLV customers.

**Stakeholders**: Product, retention, and finance teams need clear guidance on who to target.

## Key steps

1. **Exploration** (notebook 1)
   - Load customer transactions and attributes
   - Understand customer segments and purchase patterns
   - Identify data quality issues

2. **Preprocessing** (notebook 2)
   - Handle missing values
   - Create customer-level features (RFM, lifetime metrics)
   - Normalize and encode features

3. **Modeling** (notebook 3)
   - Train baseline model (linear regression or logistic classifier)
   - Compare models (tree-based, ensemble methods)
   - Evaluate with business metrics (lift, precision@k)

4. **Production** (train.py)
   - Automated training pipeline
   - Model validation and drift checks
   - Ready for inference API or batch scoring

## Recommended datasets

See `DATASETS.md` for curated public datasets with transaction histories, customer attributes, and business labels.
