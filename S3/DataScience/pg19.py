import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,ConfusionMatrixDisplay

# Load dataset
data = pd.read_csv('Titanic_Train.csv') 

# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].median())
ddata = data.fillna("Unknown")

# Encode categorical variables
le = LabelEncoder()
data['sex'] = le.fit_transform(data['sex'])
data['embarked'] = le.fit_transform(data['embarked'])

# Split features and target
X = data.drop('survived', axis=1)
y = data['survived']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# Initialize and train Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)        
dt.fit(X_train, y_train)

# Make predictions
y_pred = dt.predict(X_test)
y_proba = dt.predict_proba(X_test)[:, 1]
# Evaluate model
print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)    
plt.title('Confusion Matrix')
plt.show()

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

#viualition of decision tree
plt.figure(figsize=(20,10))
plot_tree(dt, filled=True, feature_names=X.columns, class_names=['Not Survived', 'Survived'])
plt.title('Decision Tree Visualization')
plt.show()  

