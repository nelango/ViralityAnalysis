
import pandas as pd
import numpy as np
import os
import math
from sklearn import datasets
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import normalize
# load the iris datasets
# dataset = datasets.load_iris()
def test_run():
	data1 = os.path.join("data", "data3.csv")
	dataset1 = pd.read_csv(data1)
	dataset1 = dataset1.ix[:,[2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,31,32,33,34,35,36,37,38,44,45,46,47,56,57,60]]
	dataset = dataset1.as_matrix()
	dataset_to_norm = dataset[:,0:-1]
	shares = dataset[:,-1]
	# print dataset_to_norm.shape
	dataset = normalize(dataset_to_norm)
	dataset = np.c_[dataset, shares]
 
	x = dataset[:,0:-1]
	y = dataset[:,-1]
	X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.33)
	# create a base classifier used to evaluate a subset of attributes

	model = RandomForestRegressor()
	model.fit(X_train, y_train)
	y_predict = model.predict(X_test)
	df = pd.DataFrame(y_predict)
	path = 'data/results_RF_normalized.csv'
	print model.score(X_train, y_train)
	print "done"
	# scores = cross_val_score(model, x, y)
	# print (scores.mean())
	df.to_csv(path)

if __name__ == "__main__":
    test_run()