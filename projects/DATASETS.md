# Recommended Datasets for Data Scientist Projects

Below are curated public datasets suitable for building production-ready ML projects with real business context.

## 1. E-Commerce and Customer Data

### Brazilian E-Commerce Public Dataset (Olist)
**URL**: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
**Size**: ~100k orders, 600k reviews  
**Best for**: CLV prediction, churn, recommendation, sentiment analysis  
**Columns**: orders, products, customers, payments, logistics, reviews  
**Business context**: Real marketplace with temporal data, multiple product categories, delivery delays, and customer ratings  
**Why useful**: Realistic business problem with temporal and categorical features

### UCI Online Retail Dataset
**URL**: https://archive.ics.uci.edu/dataset/352/online+retail  
**Size**: ~500k transactions, 4k products, 5k customers  
**Best for**: CLV prediction, RFM analysis, market basket analysis  
**Columns**: InvoiceNo, CustomerID, Description, Quantity, UnitPrice, Country  
**Business context**: Real online retailer transactions with product returns  
**Why useful**: Clean, well-documented, good for time-series customer analysis

### E-Commerce Events History
**URL**: https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-online-store  
**Size**: ~64M events, 560k users  
**Best for**: User funnel analysis, conversion rate prediction, recommendation  
**Columns**: event_type, product, user_id, timestamp, price  
**Business context**: Real cosmetics retailer with view→cart→purchase funnel  
**Why useful**: Large-scale event data, realistic funnel problem

---

## 2. Financial and Transactional Data

### Bank Customer Churn
**URL**: https://www.kaggle.com/datasets/churn-in-banks  
**Size**: ~10k customers  
**Best for**: Churn prediction, retention modeling, classification  
**Columns**: CustomerId, CreditScore, Age, Geography, Gender, Balance, IsActiveMember, Exited  
**Business context**: Bank customer data with clear binary outcome  
**Why useful**: Well-structured, good for stakeholder communication

### Credit Card Fraud Detection
**URL**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
**Size**: ~284k transactions, 0.17% fraud rate  
**Best for**: Fraud detection, imbalanced classification, anomaly detection  
**Columns**: Time, Amount, Class (fraud/legitimate), 28 anonymized features  
**Business context**: Realistic class imbalance problem  
**Why useful**: Teaches handling of rare events in ML

---

## 3. Supply Chain and Operations

### Instacart Market Basket Analysis
**URL**: https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis  
**Size**: ~3.2M orders, ~50k products  
**Best for**: Recommendation, market basket analysis, customer segmentation  
**Columns**: order_id, product_id, order_dow, order_hour, days_since_prior_order  
**Business context**: Real grocery delivery data with sequential purchases  
**Why useful**: Complex temporal and categorical relationships

### Supply Chain Data
**URL**: https://www.kaggle.com/datasets/shashwatwork/dataco-supply-chain-dataset  
**Size**: ~180k records  
**Best for**: Demand forecasting, delivery time prediction, logistics optimization  
**Columns**: Order Date, Delivery Date, Shipping Price, Product Category, Quantity  
**Business context**: End-to-end supply chain metrics  
**Why useful**: Real-world operational analytics

---

## 4. Customer Service and Product Data

### Airline Passenger Satisfaction
**URL**: https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction  
**Size**: ~103k passengers  
**Best for**: Satisfaction prediction, NPS modeling, feature importance  
**Columns**: Gender, Age, PassengerType, FlightDistance, Satisfaction rating  
**Business context**: Survey data with business outcome  
**Why useful**: Teaches working with customer feedback and actionable insights

### Google Reviews (Restaurant/Hotel Data)
**URL**: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset (alternative: Google Local data)  
**Size**: Varies, millions of reviews  
**Best for**: Sentiment analysis, review prediction, rating estimation  
**Columns**: review_text, rating, date, user_id, business_id  
**Business context**: Unstructured text with business outcome  
**Why useful**: Introduces NLP and feature extraction from text

---

## 5. Healthcare and Public Health

### Hospital Readmission Dataset
**URL**: https://www.kaggle.com/datasets/saurabhannadate/hospital-readmissions  
**Size**: ~100k hospital records  
**Best for**: Readmission prediction, risk stratification, intervention targeting  
**Columns**: Patient demographics, diagnoses, medications, procedures, readmission  
**Business context**: Healthcare prediction with business impact  
**Why useful**: Demonstrates model interpretability in regulated domains

### Diabetes Prediction Dataset
**URL**: https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset  
**Size**: ~100k health records  
**Best for**: Classification, risk scoring, feature selection  
**Columns**: Age, Gender, BMI, BloodPressure, Glucose, Insulin, DiabetesPedigreeFunction  
**Business context**: Healthcare classification  
**Why useful**: Clear business objective with interpretable features

---

## 6. Time Series and Forecasting

### Store Sales - Time Series Forecasting
**URL**: https://www.kaggle.com/competitions/store-sales-time-series-forecasting  
**Size**: ~3.5M records, multiple stores  
**Best for**: Time series forecasting, seasonality modeling, promotional impact  
**Columns**: Date, Store, Sales, Transactions, Promotions, Oil Prices, Holiday info  
**Business context**: Real grocery store sales with external features  
**Why useful**: Production forecasting with real business context

### AirBnB Price Prediction
**URL**: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data  
**Size**: ~49k listings  
**Best for**: Price prediction (regression), feature importance, market analysis  
**Columns**: room_type, neighbourhood, price, number_of_reviews, availability  
**Business context**: Real property pricing with temporal features  
**Why useful**: Mixed feature types (categorical, numerical, temporal)

---

## 7. HR and Recruitment

### HR Analytics Employee Attrition
**URL**: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset  
**Size**: ~1.5k employees  
**Best for**: Attrition prediction, retention modeling, HR analytics  
**Columns**: Age, Department, JobRole, MonthlyIncome, YearsAtCompany, Attrition  
**Business context**: HR decision-making  
**Why useful**: Clear business narrative for stakeholders

### Recruitment Data
**URL**: https://www.kaggle.com/datasets/saurabhshur/recruitment-data  
**Size**: ~10k candidates  
**Best for**: Hiring prediction, recruitment funnel, candidate scoring  
**Columns**: Candidate ID, Experience, Education, Interview Scores, Selected  
**Business context**: Recruitment process optimization  
**Why useful**: Demonstrates selection bias and fairness considerations

---

## 8. Telecommunications

### Telecom Customer Churn
**URL**: https://www.kaggle.com/datasets/becksddf/churn-in-telecoms-dataset  
**Size**: ~3.3k customers  
**Best for**: Churn prediction, customer segmentation, retention strategy  
**Columns**: Services subscribed, Tenure, Contract type, Monthly charges, Churn  
**Business context**: Telecom industry with clear business outcome  
**Why useful**: Good for explaining business value to non-technical stakeholders

---

## 9. Marketing and Campaigns

### Marketing Campaign Response
**URL**: https://archive.ics.uci.edu/dataset/222/bank+marketing  
**Size**: ~45k records  
**Best for**: Campaign response prediction, customer targeting, ROI modeling  
**Columns**: Demographics, previous campaigns, economic indicators, campaign result  
**Business context**: Direct marketing decision-making  
**Why useful**: Teaches handling of highly imbalanced targets and feature selection

### Customer Segmentation Dataset
**URL**: https://www.kaggle.com/datasets/adammaus/customer-segmentation-dataset  
**Size**: ~2k customers  
**Best for**: Clustering, segmentation, unsupervised learning  
**Columns**: Annual Income, Spending Score, Age, Gender  
**Business context**: Behavioral segmentation  
**Why useful**: Combines supervised and unsupervised learning

---

## 10. Natural Language Processing and Text

### Amazon Reviews Sentiment
**URL**: https://www.kaggle.com/datasets/bittlingmayer/amazon-reviews-for-sentiment-analysis  
**Size**: ~3.6M reviews  
**Best for**: Sentiment classification, text feature engineering, NLP  
**Columns**: Review text, rating (1-5)  
**Business context**: Product feedback analysis  
**Why useful**: Large-scale NLP problem with clear business value

### Fake News Detection
**URL**: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset  
**Size**: ~40k news articles  
**Best for**: Classification, text analysis, feature extraction  
**Columns**: Title, Text, Subject, Date, Label (REAL/FAKE)  
**Business context**: Content moderation and trust  
**Why useful**: Teaches working with unstructured text data

---

## How to Choose a Dataset for Your Project

| Goal | Recommended Dataset |
| --- | --- |
| **Customer LTV & Retention** | Olist E-Commerce, UCI Online Retail, Bank Churn |
| **Fraud Detection** | Credit Card Fraud, Telecom Churn |
| **Recommendation** | Instacart, E-Commerce Events |
| **Forecasting** | Store Sales, AirBnB, Airline Data |
| **Segmentation** | Customer Segmentation, Instacart |
| **NLP/Sentiment** | Amazon Reviews, Airline Satisfaction |
| **Classification** | Bank Churn, Diabetes Prediction |
| **Time Series** | Store Sales, Airline Passenger Data |

---

## Data Download Tips

1. **Kaggle**: Most datasets are on Kaggle (requires free account)
   ```bash
   pip install kaggle
   kaggle datasets download -d dataset-name
   ```

2. **UCI Machine Learning Repository**: Direct CSV downloads
   https://archive.ics.uci.edu/

3. **GitHub**: Many datasets hosted on GitHub with full notebooks

4. **API Access**: Some datasets (Yelp, Google, Twitter) available via APIs with rate limits

---

## Next Steps

1. Choose 1-2 datasets that align with your interests
2. Download and explore locally
3. Use the CLV prediction project template as your starting point
4. Adapt the workflow to your chosen dataset
5. Document your approach and results
6. Deploy and monitor (once you add MLOps practices)
