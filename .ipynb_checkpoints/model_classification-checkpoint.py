## Machine Learning Model Prediction

'''
Since the data is classifying/identifying diagnosis status, we want to determine
if subject has heart disease (yes/no). Therefore, we should run a Supervised ML,
Logistic Regression Model. 
'''

# Dependencies
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.preprocessing as preprocessing
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Import cleaned preprocessed data
path = "C:/Users/Kanna/HeartDisease_Classification"
heart_data = pd.read_csv(path+"./heartdisease.csv")

# Display data
heart_data

heart_data.columns

## Further preprocessing data
# Further clean data - remove "Unnamed: 0" column
heart_data = heart_data.drop(columns=['Unnamed: 0'])

# Verify
heart_data.columns

# Change Diagnosis column so we only have 0 and 1 (absense and presence)
# Copy data
heart_new = heart_data.copy()

heart_new['Diagnosis'].head()

# Change
heart_new['Diagnosis'].values[heart_new['Diagnosis'] > 0] = 1

# Verify
heart_new['Diagnosis'].head()

## Implement Logistic Regression Model
# Identify Target variable
y = heart_new['Diagnosis']

# Identify Feature variables
X = heart_new.drop(['Diagnosis'], axis=1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.25, 
                                                    random_state=42)

import warnings
from sklearn.exceptions import ConvergenceWarning

# Ignore ConvergenceWarning
warnings.filterwarnings("ignore", category = ConvergenceWarning)

# Classify Logistic Regression Model
classifier1 = LogisticRegression(solver = 'lbfgs', random_state=0)
classifier1

classifier2 = LogisticRegression(solver = 'sag', random_state=0)
classifier2
    # Used as solver for large datasets

# Fit and train the data
classifier1.fit(X_train, y_train)
classifier2.fit(X_train, y_train)

# Evaluate the models
print("Evaluating Probability Scores")
print("-"*35)

print("Logistic Regression Model Solver 'lbfgs':\n {}"
      .format(classifier1.score(X_train, y_train)))

print("-"*35)

print("Logistic Regression Model Solver 'sag':\n {}"
      .format(classifier2.score(X_train, y_train)))

## Make Predictions
# Predict outcomes for test data
predictions1 = classifier1.predict(X_test)
predictions2 = classifier2.predict(X_test)

# Calculate Accuracy Score
accuracy_score1 = accuracy_score(y_test, predictions1)
accuracy_score2 = accuracy_score(y_test, predictions2)

print("Evaluating Accuracy Scores")
print("-"*35)

print("Logistic Regression Model Solver 'lbfgs':\n {}"
      .format(accuracy_score1))

print("-"*35)

print("Logistic Regression Model Solver 'sag':\n {}"
      .format(accuracy_score2))

'''
Logistic Regression Model solver 'lbfgs' proves to be better based on
accuracy score of 77.7%.
'''

## Confusion Matrix
print("Confusion Matrix")
print("-"*35)
print(confusion_matrix(y_test, predictions1))

## Classification Report
target_names = ["Absence of HD", "Presence of HD"]
print(classification_report(y_test, predictions1, target_names=target_names))
