# -*- coding: utf-8 -*-
"""
Random Forest Accident Severity Classification
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Data_Final.csv")

data['Severity_Class'] = data['SEVERITY'].apply(lambda x: "HIGH" if x >= 2 else "MODERATE")

features = ['DAY_OF_WEEK','LIGHT_CONDITION','ALCOHOLTIME','SPEED_ZONE']
X = data[features]
y = data['Severity_Class']

X = X.fillna("Unknown")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("Classification Report (Random Forest):")
print(classification_report(y_test, y_pred))

importances = rf.feature_importances_
sns.barplot(x=importances, y=features)
plt.title("Feature Importance for Accident Severity")
plt.show()
