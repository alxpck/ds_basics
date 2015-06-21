from s2v3 import *

# Find the average
def find_average(data_sample, header=False): #update the function to avoid having to use slices to skip over header rows
	if header: # this is the way to check to see if an argument exists
		data_sample = data_sample[1:]
	total = calculate_sum(data_sample)
	size = number_of_records(data_sample)
	average = total / size
	return average

average_price = find_average(data_from_csv, True) # Second argument takes a boolean value that indicates if the data_sample has headers. Above we've set the default value to False (which makes this an optional argument), but if we set it to True it means we want to skip the first row. Now, see I think I'd just set the default to True so that the function always skipped the first row (the headers). It's less complicated that way. Most of the time we're going to want to work with the non-header values, not the headers, so I feel like we should make getting at the headers a non-default option and keep the majority cases as the defualt.

print("Average =", average_price) # no need to add spaces because "," seems to automatically add one (at least in the print function)

print('{:03.2f}'.format(average_price)) 

# string formatting function for two decimal points
# 0X. sets the number of decimal places in front of the decimal point
# .Xf sets teh number of decimal places behind the decimal point