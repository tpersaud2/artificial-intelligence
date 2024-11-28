import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

cardata = pd.read_csv('CAR DETAILS FROM CAR DEKHO.csv')
print(cardata.head())

cardata = pd.get_dummies(cardata, drop_first=True)

cardata = cardata.dropna()
X = cardata.drop('selling_price', axis=1)
y = cardata['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 43)

lr = LinearRegression()
lr.fit(X_train, y_train)
predicted_value = lr.predict(X_test)

mse = mean_squared_error(y_test, predicted_value)
mae = mean_absolute_error(y_test, predicted_value)
print("Mean Squared Error: ", mse)
print("Mean Absolute Error: ", mae)
