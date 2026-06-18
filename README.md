# Fraud Detection System using Machine Learning

## Project Overview

This project aims to detect fraudulent financial transactions using Machine Learning techniques on a large-scale transaction dataset containing more than 1.9 million records.

The objective is to accurately identify fraudulent transactions while minimizing false alarms on legitimate transactions. The project goes beyond a basic fraud detection notebook by incorporating multiple machine learning models, class imbalance handling, threshold optimization, explainability techniques, business impact analysis, and an interactive web application for deployment.

---

## Problem Statement

Fraudulent financial transactions cause significant monetary losses and are challenging to identify because fraudulent transactions represent only a very small fraction of all transactions.

This project addresses this challenge by building a robust fraud detection pipeline capable of identifying suspicious transactions while maintaining a low false positive rate.

---

## Dataset

**Dataset:** PaySim Synthetic Financial Dataset

The dataset contains over 1.9 million transactions with information such as:

* Transaction type
* Transaction amount
* Sender account balances
* Receiver account balances
* Fraud labels

The dataset is intentionally excluded from this repository due to its large size.

---

## Feature Engineering

Additional features were created to improve model performance.

Engineered features:

* `balanceDiffOrig`
* `balanceDiffDest`

These features capture balance changes before and after transactions and provide additional fraud-related signals.

---

## Machine Learning Pipeline

The project pipeline consists of:

1. Data Cleaning and Preprocessing
2. Feature Engineering
3. Model Training
4. Class Imbalance Handling
5. Model Evaluation
6. Threshold Optimization
7. Explainability Analysis
8. Business Impact Analysis
9. Model Deployment

---

## Models Trained

The following models were trained and compared:

### Baseline Models

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM

### SMOTE Enhanced Models

* SMOTE + Logistic Regression
* SMOTE + KNN
* SMOTE + Random Forest
* SMOTE + Gradient Boosting
* SMOTE + XGBoost
* SMOTE + LightGBM

---

## Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Precision-Recall AUC

Since fraud detection is a highly imbalanced classification problem, special emphasis was placed on Recall, F1 Score, and minimizing false positives instead of relying solely on Accuracy.

---

## Threshold Optimization

Default classification thresholds are often suboptimal for fraud detection systems.

A threshold optimization phase was implemented to determine a better decision threshold that balances:

* Fraud detection capability
* False alarm reduction
* Business usability

---

## Explainability Analysis

Model interpretability was incorporated through:

* SHAP analysis
* Feature Importance Analysis

Important fraud indicators included:

* oldbalanceOrg
* newbalanceOrig
* amount
* type_TRANSFER
* balanceDiffOrig
* balanceDiffDest

---

## Business Impact Analysis

The project also evaluates real-world performance by measuring:

* Frauds correctly detected
* Frauds missed
* Legitimate transactions incorrectly flagged

This provides a practical perspective beyond traditional ML metrics.

---

## Web Application

A Streamlit web application was developed to allow users to enter transaction details and obtain fraud predictions interactively.

The application:

* Accepts transaction information
* Performs preprocessing automatically
* Calculates engineered features
* Displays fraud probability
* Displays fraud risk prediction

---

## Model Training and Deployment Strategy

Multiple models were trained and exported during experimentation and comparison.

The original final Random Forest model was trained on the complete dataset, resulting in a large serialized model file.

To improve repository portability and deployment usability, a lightweight deployment-oriented Random Forest model was subsequently trained and included in this repository.

The original larger model is preserved locally for experimentation purposes.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* XGBoost
* LightGBM
* SHAP
* Matplotlib
* Streamlit
* Joblib

---

## Project Structure

```
Fraud-Detection-System/

analysis_model.ipynb

fraud_detection.py

models/
fraud_small.pkl

results/
business_impact.csv
comparison_df.csv
feature_importance.csv
feature_importance.png
smote_comparison_df.csv

requirements.txt

README.md
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run fraud_detection.py
```

---

## Future Improvements

* Real-time fraud monitoring
* Cloud deployment
* API integration
* Live transaction streaming
* Model retraining pipelines

