#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm

#clf = svm.SVC(kernel = 'linear') #accuracy: 0.884527872582 for 1% data
clf = svm.SVC(C = 10000.0, kernel = 'rbf') 
#C = 10.0 accuracy: 0.616040955631 for 1% data
#C = 100.0 accuracy: 0.616040955631 for 1% data
#C = 1000.0 accuracy: 0.821387940842 for 1% data
#C = 10000.0 accuracy: 0.892491467577 for 1% data, 0.990898748578 for 100% data



#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf = clf.fit(features_train, labels_train)
print "fitting time:", round(time()-t0, 3), "s"


tp = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-tp, 3), "s"

print "answer_10:", pred[10]
print "answer_26:", pred[26]
print "answer_50:", pred[50]

count = 0
for i in range(len(features_test)):
    if pred[i] == 1:
        count = count + 1

print "Number of Chris(1) class:", count

accuracy = clf.score(features_test, labels_test)

print "accuracy:", accuracy

#########################################################


