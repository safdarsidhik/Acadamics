import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score

# Load dataset
data = pd.read_csv('Titanic_Train.csv')

#select relevant features and target variable
features = data[["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]]
target = data['Survived'] 

# Handle missing values
features['Age'].fillna(features['Age'].median(), inplace=True) 

# Encode categorical variables
le = LabelEncoder()
features['Sex'] = le.fit_transform(features['Sex'])

#Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Make predictions
y_pred = rf.predict(X_test)
y_proba = rf.predict_proba(X_test)[:, 1]        

# Evaluate model
print("Confusion Matrix:")  
print(confusion_matrix(y_test, y_pred))

plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix Heatmap')
plt.show()


print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_proba))

# Feature importance
importances = rf.feature_importances_
feature_names = features.columns

plt.figure(figsize=(10,6))
plt.barh(importances,feature_names)
plt.title('Feature Importances')
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.show()

# Compare n estimators
n_estimators = [10, 50, 100, 200]

for n in n_estimators:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f'Accuracy with {n} estimators: {acc:.4f}')