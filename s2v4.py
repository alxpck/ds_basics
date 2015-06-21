from s2v3 import *

# Find the average
def find_average(data_sample, header=False): #update the function to avoid having to use slices to skip over header rows
	if header: # this is the way to check to see if an argument exists
		data_sample = data_sample[1:]
	total = calculate_sum(data_sample)
	size = number_of_records(data_sample)
	average = total / size
	return average

average_price = find_average(data_from_csv, True) 
	# Second argument takes a boolean value that indicates if the data_sample has headers. Above we've set the default value to False (which makes this an optional argument), but if we set it to True it means we want to skip the first row. Now, see I think I'd just set the default to True so that the function always skipped the first row (the headers). It's less complicated that way. Most of the time we're going to want to work with the non-header values, not the headers, so I feel like we should make getting at the headers a non-default option and keep the majority cases as the defualt.

# print("Average =", average_price) # no need to add spaces because "," seems to automatically add one (at least in the print function)

# print('{:03.2f}'.format(average_price)) 

# string formatting function for decimal places
# 0X. sets the number of decimal places in front of the decimal point
# .Xf sets teh number of decimal places behind the decimal point


# print("float version", average_price, "integer version", int(average_price))
# print(type(int(average_price))) # class integer
# print(type(average_price)) # class float
# print(type(data_from_csv)) # class list
# print(type(my_csv)) # class numpy.ndarray

midpoint = round(number_of_ties / 2) 
	# round up or down as necessary and in doing so convert it to an integer value. Python lists require you to enter an integer value to indicate the index. Counting the number of ties, dividing the number (len()) in half, and then rouding it up or down to an integer, gives us the midpoint number. It turns out the midpoint number also equals the ID or index value of the midpoint entry in the data. That means we can use data_sample[midpoint] to pull up the entry at the midpoint. 
	
	# midpoint = median

	# median = In statistics and probability theory, the median is the number separating the higher half of a data sample, a population, or a probability distribution, from the lower half.

	# wouldn't it just be easier to always say midpoint? I think so. 

message = "Average of {} half = ${:03.2f}" # {} is a place holder for a future value, much like "blah blah blah %s is this" % value. The {} placeholder with formatting inside lets us format the string value to three places before the decimal and two after

# print(message.format("1st", find_average(data_from_csv[:midpoint], True))) # True = there is a header
# print(message.format("2nd", find_average(data_from_csv[midpoint:], False))) # False = there is not a header





