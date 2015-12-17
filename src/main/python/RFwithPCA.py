
import pandas as pd
import numpy as np
import os
import math
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn import metrics
# from sklearn.tree import DecisionTreeRegressor #RandomForestClassifier #Classifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn import preprocessing

# load the iris datasets
# dataset = datasets.load_iris()
def test_run():	
	data1 = os.path.join("data", "data3.csv")
	dataset1 = pd.read_csv(data1)
	number = preprocessing.LabelEncoder()
	dataset1.apply(number.fit_transform)
	# print dataset1.ix[1:5]
	dataset = dataset1.as_matrix()
	x = dataset[:,1:60]
	y = dataset[:,60]
	X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=.33)
	# # y = dataset[:,60]
	# x_ =x[0:10000,:]
	# # y = dataset[0:10000,60]
	# y_ = y[0:10000]
	# x_test = x[11001:12001,:]
	# # y_test = dataset[1001:1201, -1].astype(int)
	# y_test = y[11001:12001]
	# print y_test
	# create a base classifier used to evaluate a subset of attributes
	print "starting"
	pca = PCA()#n_components = 2)#DecisionTreeRegressor() #RandomForestClassifier() #ExtraTreesClassifier()
	X_reduced = pca.fit_transform(scale(X_train))
	model = RandomForestRegressor() #ExtraTreesClassifier()
	model.fit(scale(X_reduced), y_train)
	print (model.score(scale(X_test),y_test))
	y_predict = model.predict(scale(X_test))
	df = pd.DataFrame(y_predict)
	path = 'data/results_RF_PCA.csv'
	# print (model.explained_variance_ratio_)
	print "done"
	# scores = cross_val_score(model, x, y)
	# print (scores.mean())
	df.to_csv(path)

if __name__ == "__main__":
    test_run()
