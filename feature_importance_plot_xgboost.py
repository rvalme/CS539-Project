# plot feature importance using built-in function
from numpy import loadtxt
from xgboost import XGBClassifier
from xgboost import plot_importance
from matplotlib import pyplot
import pandas as pd
# load data
dataset = pd.read_csv('2017_USCensus_Cleaned.csv')
# split data into X and y
X = dataset.drop(['Unnamed: 0', 'ZIP', 'Count'], axis=1)
y = dataset.Count
# fit model no training data
model = XGBClassifier()
model.fit(X, y)
# plot feature importance
plot_importance(model)
pyplot.show()