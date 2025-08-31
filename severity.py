import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('Data_Final.csv')
X = dataset.iloc[:,:].values
X = np.delete(X,2,axis=1)
X = np.delete(X,1,axis=1)
X = np.delete(X,0,axis=1)
names = (dataset.columns.values)
names = names[3:]

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
X[:,:] = imputer.fit_transform(X[:,:])
data_new = pd.DataFrame(data=X, columns=names)

plt.figure(figsize=(30,8))
sns.countplot(x='LIGHT_CONDITION', hue='SEVERITY', data=data_new)
plt.savefig("Snapshots/severity_light_condition.png")

plt.figure(figsize=(30,8))
sns.countplot(x='SEVERITY', hue='ALCOHOLTIME', data=data_new)
plt.savefig("Snapshots/severity_alcohol.png")

plt.figure(figsize=(30,8))
sns.countplot(x='LIGHT_CONDITION', hue='ALCOHOLTIME', data=data_new)
plt.savefig("Snapshots/light_vs_alcohol.png")

plt.figure(figsize=(30,8))
sns.countplot(x='SEVERITY', hue='SPEED_ZONE', data=data_new)
plt.savefig("Snapshots/severity_speed_zone.png")

plt.figure(figsize=(30,8))
sns.countplot(x='POLICE_ATTEND', hue='SPEED_ZONE', data=data_new)
plt.savefig("Snapshots/police_vs_speedzone.png")

plt.figure(figsize=(30,8))
sns.countplot(x='FEMALES', hue='SEVERITY', data=data_new)
plt.savefig("Snapshots/females_vs_severity.png")

print("Plots saved in Snapshots/ folder")
