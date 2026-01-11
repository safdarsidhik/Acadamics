"""
Decision Tree Classifier on Wine Quality Dataset
Evaluates model accuracy, confusion matrix, precision/recall/F1, 
classification report, tree visualization, and comparison of
Gini vs Entropy criteria.

Make sure the wine quality dataset CSV file (red or white wine) is in the same folder.
Set DATA_PATH accordingly.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------------------
# STEP 1: Load Dataset
# -----------------------------------------
DATA_PATH = "winequality.csv"   # change this to your file name
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded — shape:", df.shape)
print(df.head())

# target column usually named "quality"
target = "quality"
X = df.drop(columns=[target])
y = df[target]

# -----------------------------------------
# STEP 2: Train-Test Split
# -----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------------------
# STEP 3: Train Decision Tree (Gini)
# -----------------------------------------
model_gini = DecisionTreeClassifier(criterion="gini", random_state=42)
model_gini.fit(X_train, y_train)

y_pred_gini = model_gini.predict(X_test)

# -----------------------------------------
# STEP 4: Accuracy
# -----------------------------------------
accuracy = accuracy_score(y_test, y_pred_gini)
print("\n1. Accuracy (Gini):", accuracy)

# -----------------------------------------
# STEP 5: Confusion Matrix
# -----------------------------------------
cm = confusion_matrix(y_test, y_pred_gini)
print("\n2. Confusion Matrix:\n", cm)

# -----------------------------------------
# STEP 6: Precision, Recall, F1
# -----------------------------------------
print("\n3. Precision / Recall / F1-score:")
print(classification_report(y_test, y_pred_gini))

# -----------------------------------------
# STEP 7: Visualize Decision Tree
# -----------------------------------------
plt.figure(figsize=(16,10))
plot_tree(model_gini, feature_names=X.columns, class_names=[str(c) for c in sorted(y.unique())], filled=True, fontsize=7)
plt.title("Decision Tree (Gini)")
plt.show()

print("\n5. Decision Path Explanation:")
print("Follow the plotted tree: it splits using thresholds on features like alcohol, pH, sulphates, etc.")
print("Example Interpretation: If alcohol > X and volatile acidity < Y then predicted quality = Z.")

# -----------------------------------------
# STEP 8: Compare Gini vs Entropy
# -----------------------------------------
model_entropy = DecisionTreeClassifier(criterion="entropy", random_state=42)
model_entropy.fit(X_train, y_train)
y_pred_entropy = model_entropy.predict(X_test)

acc_entropy = accuracy_score(y_test, y_pred_entropy)
print("\n6. Comparison of Criteria:")
print(f"Accuracy using Gini:    {accuracy}")
print(f"Accuracy using Entropy: {acc_entropy}")

print("Classification Report (Entropy):")
print(classification_report(y_test, y_pred_entropy))

print("PROGRAM COMPLETE — all evaluation metrics generated.")
