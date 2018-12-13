from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor

import sys

# load data
dataset = pd.read_csv('Combined_Count.csv')
dataset = dataset.astype(float)


def MachineLearningAlgorithm(dataset, features_in_order):

	try:
		ml_algorithm_choice = int(sys.argv[1])
	except:
		print('Please choose machine learning algorithm:\n\t1) XGBoost\n\t2) neural network\n\t3) Linear regression')
		return

	#output file name
	#ml algorithm
	if(ml_algorithm_choice == 1):
		output_file_name = 'XGBoost'
		model = XGBClassifier()
	elif(ml_algorithm_choice == 2):
		output_file_name = 'NeuralNetworks'
		model = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 3), random_state=1)
	elif(ml_algorithm_choice == 3):
		output_file_name = 'LinearRegression'
		model = LinearRegression()
	else:
		print('Invalid choice')
		return



	i = 1
	split_index = 66238
	while i <= len(features_in_order):

		#Initiliaze data
		seed = 7
		test_size = 0.33

		X = dataset[features_in_order[0:i] + ['ZIP']].copy()
		Y = dataset.Count

		#Split the data
		X_train, X_test, y_train, y_test = X[:66238], X[66238:], Y[:66238], Y[66238:]
		zipcodes = X_test.ZIP

		X_test = X_test.drop(['ZIP'], axis = 1)
		X_train = X_train.drop(['ZIP'], axis = 1)

		#Fit the model
		model.fit(X_train, y_train)

		#Measure performance
		y_pred = model.predict(X_test)
		y_pred = np.clip(y_pred, 0., 30.)
		y_pred = np.round(y_pred, decimals=0)
		#y_pred = np.ceil(y_pred)
		print(1 - (np.count_nonzero(y_test-y_pred)/len(y_test)))


		i = i + 1


	#Initiliaze data
	seed = 7
	test_size = 0.33

	X = dataset.drop(['Unnamed: 0', 'Count'], axis=1)
	Y = dataset.Count

	#X_train, X_test, y_train, y_test = train_test_split(X,  Y, test_size=test_size, random_state=seed)
	X_train, X_test, y_train, y_test = X[:66238], X[66238:], Y[:66238], Y[66238:]
	zipcodes = X_test.ZIP

	X_test = X_test.drop(['ZIP'], axis = 1)
	X_train = X_train.drop(['ZIP'], axis = 1)

	# fit model no training data
	model.fit(X_train, y_train)
	print(model)

	# make predictions for test data
	y_pred = model.predict(X_test)
	predictions = [round(value) for value in y_pred]

	# evaluate predictions
	accuracy = accuracy_score(y_test, predictions)
	print("Accuracy: %.2f%%" % (accuracy * 100.0))



	#Save the output file
	df = pd.DataFrame (np.column_stack(( zipcodes, y_test, y_pred)))
	filepath = output_file_name + '.xlsx' 
	df.to_excel(filepath, index=False)





def Main():


	feature_in_order = ['Total; Estimate; NONFAMILY HOUSEHOLDS - Nonfamily households',
						'Total; Estimate; One race-- - Asian',
						'Total; Estimate; FAMILIES - Female householder, no husband present',
						'Total; Estimate; One race-- - Black or African American',
						'Total; Estimate; Two or more races',
						'Total; Estimate; NONFAMILY HOUSEHOLDS - Male householder',
						'Total; Estimate; NONFAMILY HOUSEHOLDS - Male householder - Not living alone',
						'Total; Estimate; Hispanic or Latino origin (of any race)',
						'Total; Estimate; HOUSEHOLD INCOME BY AGE OF HOUSEHOLDER - 25 to 44 years',
						'Total; Estimate; FAMILIES - Families',
						'Total; Estimate; HOUSEHOLD INCOME BY AGE OF HOUSEHOLDER - 65 years and over',
						'Median income (dollars); Estimate; FAMILIES - Families - With no own children under 18 years',
						'Median income (dollars); Estimate; NONFAMILY HOUSEHOLDS - Male householder',
						'Median income (dollars); Estimate; HOUSEHOLD INCOME BY AGE OF HOUSEHOLDER - 15 to 24 years',
						'Median income (dollars); Estimate; HOUSEHOLD INCOME BY AGE OF HOUSEHOLDER - 65 years and over',
						'Median income (dollars); Estimate; NONFAMILY HOUSEHOLDS - Male householder']


	MachineLearningAlgorithm(dataset, feature_in_order)




def AggragateZipCodeResults():
	dataset = pd.read_excel('LinearRegression.xlsx')
	dataset = dataset.astype(int)
	dataset['0'] = dataset['0'].astype(str).str[:-2].astype(np.int64)
	print(dataset)



Main()


