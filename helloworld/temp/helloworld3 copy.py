import numpy as np
import csv
# my_data = np.genfromtxt('data3.csv', delimiter=',')
# print type(my_data)
# f = open("data4.csv", "r")
# reader = csv.reader(f, delimiter=',')
# for row in reader:
#     print '\t'.join(row)
# # my_list = list(reader)
# # print my_list
# # lines = f.read().split("\n")
# # print type(lines)

# # for line in lines:
# #     if line != "": # add other needed checks to skip titles
# #         cols = line.split(",")
# #         print cols
class KNNLearner:
    def __init__(self, k=3):
        self.k = k
        self.Xtrain = []
        self.Ytrain = []

    def addEvidence(self, Xtrain, Ytrain):
    	self.Xtrain = Xtrain
    	self.Ytrain = Ytrain

    def query(self, Xtest):
    	train = np.c_[self.Xtrain, self.Ytrain]
    	print train.shape[1]
    	delta = []	
    	for j in range(train.shape[0]):
    		dist = 0
    		for i in range(len(Xtest)):
    			dist = dist + (train[j][i] - Xtest[i])**2
    		dist = np.sqrt(dist)
    		delta.append(dist)
    	delta = np.c_[delta, train]
    		# delta = np.sort(delta)
    	delta = delta[delta[:,0].argsort()]
    	delta = delta[0:self.k]
    	mean = delta[:,-1].mean()
    	Ytest = mean
        # print delta
    	return Ytest

with open("data4.csv", 'r') as f:
	data = [row for row in csv.reader(f.read().splitlines())]
data = np.array(data)
# dataset1 = dataset1.ix[:,[2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,31,32,33,34,35,36,37,38,44,45,46,47,56,57,60]]
data = data[1:,[1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,30,31,32,33,34,35,36,37,43,44,45,46,47,48,55,56,59]]
data = data.astype(np.float)
X = data[:,0:-1]
trainX = data[:-1,0:-1]
print trainX.shape
trainY = data[:-1,-1]
learner = KNNLearner(k = 3) # constructor
testX = [1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,30,31,32,33,34,35,36,37,43,44,45,46,47,48,55,56]
print len(testX)

learner.addEvidence(trainX, trainY) # training step
predY = learner.query(testX) # get the predictions
print int(predY)
ns = [1,2,3]
sn = [4,5,6]
ns = ns+sn
print type(ns)
# ns = ns.append([4,5,6])
# rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])

# print "In sample results"
# print "RMSE: ", rmse
# c = np.corrcoef(predY, y=trainY)
# print "corr: ", c[0,1]