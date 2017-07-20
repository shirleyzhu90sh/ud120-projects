#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### the nunber of people
datakeys = list(enron_data.keys())
print "the nunber of people:", len(datakeys)

### the feature number of people
print "the feature number of people:", len(list(enron_data["SKILLING JEFFREY K"]))

### the number of poi in dataset
count = 0
for person_name in datakeys:
    if enron_data[person_name]["poi"]==1:
        count = count + 1

print "the number of poi in dataset:", count

### the number of poi in poi_names
poi_names=r"../final_project/poi_names.txt"
fp=open(poi_names)
link = fp.readline()
blank = fp.readline()
arr=[]
for names in fp.readlines():
    names=names.replace("\n","")
    arr.append(names)
fp.close()
print "the number of poi in poi_names:", len(arr)

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]

#print datakeys
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

count_eff_salary = 0
count_eff_email = 0
count_eff_total_payments = 0

for name in datakeys:
    if enron_data[name]["salary"] != 'NaN':
        count_eff_salary = count_eff_salary + 1
    if enron_data[name]["email_address"] != 'NaN':
        count_eff_email = count_eff_email + 1
    if enron_data[name]["total_payments"] != 'NaN' and enron_data[name]["poi"]==1:
        count_eff_total_payments = count_eff_total_payments + 1
print count_eff_salary, count_eff_email, count_eff_total_payments