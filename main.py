import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

heartdata = pd.read_csv("cleaned_merged_heart_dataset.csv")
print(heartdata.head())

X = heartdata.drop(columns=['target'])
y = heartdata['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

heartmodel = DecisionTreeClassifier(criterion='gini', random_state=1)
heartmodel.fit(X_train, y_train)

y_pred = heartmodel.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
