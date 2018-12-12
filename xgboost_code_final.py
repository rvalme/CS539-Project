from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# load data
dataset = pd.read_csv('2017_USCensus_Cleaned.csv')
# split data into X and y
X = dataset[['Total; Estimate; Households', 
]].copy()
Y = dataset.Count

print(X)
print(Y)
						
seed = 7
test_size = 0.66
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
print(model)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

prediction = pd.DataFrame(y_pred, columns=['predictions'])
newdf = pd.concat([dataset, prediction], axis=1)
newdf.to_csv('results_xgboost.csv')			

# The mean squared error

#print("Mean squared error: %.2f" % np.mean((regressor.predict(X_test) - y_test) ** 2))

# Explained variance score: 1 is perfect prediction

#print('Variance score: %.2f' % regressor.score(X_test, y_test))			


