import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("Credit Card Customer Data.csv")

print("Data Preview:\n", data.head())
print("\nData Information:\n")
print(data.info())

if data.isnull().sum().any():
    data = data.dropna()

numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
X = data[numerical_columns]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

sse = []
k_range = range(1, 11)

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X_scaled)
    sse.append(km.inertia_)

sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.lineplot(x=list(k_range), y=sse)
plt.xlabel("Number of clusters (k)")
plt.ylabel("Sum Squared Error")
plt.title("Elbow Method")
plt.show()

k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_scaled)

data['Cluster'] = kmeans.labels_

print("\nCluster Centers:\n", kmeans.cluster_centers_)

cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=numerical_columns)
print("\nCluster Centers (Original Scale):\n", cluster_centers_df)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
    plt.scatter(center[0], center[1], marker='^', c='red')
plt.xlabel(numerical_columns[0])
plt.ylabel(numerical_columns[1])
plt.title("Cluster Visualization (Features 1 & 2)")

plt.subplot(1, 2, 2)
plt.scatter(X_scaled[:, 2], X_scaled[:, 3], c=kmeans.labels_, cmap=cm.Accent)
plt.grid(True)
for center in kmeans.cluster_centers_:
    plt.scatter(center[2], center[3], marker='^', c='red')
plt.xlabel(numerical_columns[2])
plt.ylabel(numerical_columns[3])
plt.title("Cluster Visualization (Features 3 & 4)")

plt.tight_layout()
plt.show()
