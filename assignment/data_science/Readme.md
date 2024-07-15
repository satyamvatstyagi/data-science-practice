
## Summary of Steps Taken

### 1. Data Loading:
- The dataset "US_Heart_Patients.csv" was successfully loaded into the program using a random seed of 42 for consistency.

### 2. Exploratory Data Analysis (EDA):
- **Initial Data Exploration:**
  - Reviewed the first 10 rows of the dataset to understand its structure and content.
  - Computed the 5-point summary (min, Q1, median, Q3, max) for numerical columns to grasp the data distribution.
  - Examined column data types to ensure compatibility with modeling techniques.
  
- **Data Quality Check:**
  - Identified and addressed missing values, ensuring data completeness.
  - Detected and handled outliers to prevent them from skewing model performance.
  
- **Statistical Insights:**
  - Explored correlations between variables to understand potential relationships.
  - Visualized data distributions through histograms and box plots to assess data spread and skewness.

### 3. Data Preprocessing:
- **Missing Value Imputation:**
  - Employed appropriate techniques (e.g., mean, median imputation) to fill missing values where necessary.

- **Outlier Treatment:**
  - Applied methods (e.g., IQR method) to handle outliers, ensuring they do not adversely affect model training.

- **Categorical Feature Encoding:**
  - Encoded categorical variables using techniques such as one-hot encoding for compatibility with machine learning models.

### 4. Dataset Splitting:
- Split the dataset into 80% training and 20% test sets to facilitate model training and evaluation.

### 5. Model Preparation and Evaluation:
- **Model Evaluation:**
  - Implemented Naïve Bayes and Decision Tree algorithms for prediction.
  - Trained models on the training dataset and evaluated performance on both training and test data.

- **Performance Metrics:**
  - Calculated the F1 score for each model to assess predictive accuracy.
  - Selected the best-performing model based on the F1 score and provided an explanation.

- **Performance Analysis:**
  - Interpreted the confusion matrix and classification report of the chosen model to gain insights into its predictive capabilities.

---

## Explaination for the evaluation metrics and the classification reports for both the Naive Bayes and Decision Tree models:

### Accuracy
Accuracy measures the proportion of correctly predicted instances out of the total instances.

- **High Accuracy** indicates that the model is performing well overall, but it can be misleading in the case of imbalanced datasets.

### Precision
Precision measures the proportion of correctly predicted positive instances out of all instances predicted as positive.

- **High Precision** indicates that the model has a low false positive rate.

### Recall (Sensitivity or True Positive Rate)
Recall measures the proportion of correctly predicted positive instances out of all actual positive instances.

- **High Recall** indicates that the model has a low false negative rate.

### F1 Score
The F1 score is the harmonic mean of precision and recall. It balances the trade-off between precision and recall.

- **High F1 Score** indicates that the model performs well in terms of both precision and recall.

## Naive Bayes - Evaluation Metrics

### Metrics:
- **Accuracy**: 63.79%
- **Precision**: 73.19%
- **Recall**: 39.34%
- **F1 Score**: 51.17%

### Classification Report:
- **Class 0 (No Heart Attack)**:
  - Precision: 61%
  - Recall: 87%
  - F1 Score: 71%
  - Support: 745 samples
- **Class 1 (Heart Attack)**:
  - Precision: 73%
  - Recall: 39%
  - F1 Score: 51%
  - Support: 694 samples

### Explanation:
- **Accuracy** of 63.79% indicates that the Naive Bayes model correctly predicted about 64% of the instances overall.
- **Precision** of 73.19% for class 1 (Heart Attack) means that when the model predicts a heart attack, it is correct about 73% of the time.
- **Recall** of 39.34% for class 1 indicates that the model correctly identifies about 39% of actual heart attack cases.
- **F1 Score** of 51.17% balances the precision and recall, showing moderate performance in predicting heart attacks.
- The **high recall for class 0 (No Heart Attack)** at 87% suggests that the model is better at identifying non-heart attack cases, but **lower recall for class 1** suggests it misses a significant number of actual heart attack cases.

## Decision Tree - Evaluation Metrics

### Metrics:
- **Accuracy**: 81.79%
- **Precision**: 83.44%
- **Recall**: 77.67%
- **F1 Score**: 80.45%

### Classification Report:
- **Class 0 (No Heart Attack)**:
  - Precision: 80%
  - Recall: 86%
  - F1 Score: 83%
  - Support: 745 samples
- **Class 1 (Heart Attack)**:
  - Precision: 83%
  - Recall: 78%
  - F1 Score: 80%
  - Support: 694 samples

### Explanation:
- **Accuracy** of 81.79% indicates that the Decision Tree model correctly predicted about 82% of the instances overall.
- **Precision** of 83.44% for class 1 (Heart Attack) means that when the model predicts a heart attack, it is correct about 83% of the time.
- **Recall** of 77.67% for class 1 indicates that the model correctly identifies about 78% of actual heart attack cases.
- **F1 Score** of 80.45% balances the precision and recall, showing good performance in predicting heart attacks.
- **High precision and recall for class 0 (No Heart Attack)** suggest that the model is effective at distinguishing between heart attack and non-heart attack cases. It performs well in correctly identifying true positives and minimizing false negatives and false positives.

## Conclusion:
- **Naive Bayes**: The model shows moderate performance with a significant trade-off between precision and recall for heart attack prediction. It is more likely to miss actual heart attack cases, as indicated by its lower recall.
- **Decision Tree**: The model shows excellent performance with high accuracy, precision, recall, and F1 scores. It is effective at correctly identifying both heart attack and non-heart attack cases, making it a better choice for this dataset.

The Decision Tree model significantly outperforms the Naive Bayes model, making it the preferred model for predicting heart attack risk in this dataset.

---