#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree

clf = tree.DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf = clf.fit(features_train, labels_train)
print "fitting time:", round(time()-t0, 3), "s"

acc_min_samples_split_40 = clf.score(features_test, labels_test)
print "acc_min_samples_split_40", round(acc_min_samples_split_40, 3)

print len(features_train[0]) #feature number which can be changed by 
#modifing 'selector = SelectPercentile(f_classif, percentile=1)' in email_preporcess.py
#when percentile = 10, feature number = 3785
#when percentile = 1, feature number = 379

#########################################################


