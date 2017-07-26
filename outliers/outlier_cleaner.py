#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    whole_data = []
    from operator import itemgetter

    for i in range(len(ages)):
        whole_data.append((ages[i], net_worths[i], abs(predictions[i]-net_worths[i])))
    whole_data.sort(key=itemgetter(2))
    cleaned_data = whole_data[:80]

    return cleaned_data

