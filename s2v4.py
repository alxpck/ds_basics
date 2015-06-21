from s2v3 import *

def find_average(data_sample):
	total = calculate_sum(data_sample)
	size = number_of_records(data_sample)
	average = total / size
	return average

average_price = find_average(data_from_csv[1:]) # here we go slicing our way past the header row again, I just think that's a stupid way to handle this. I feel like we shoul always munge the data so that headers are automatically not included. See what I did with munge there? Yeah, I'm getting into the terminology

print("Average is", average_price) # no need to add spaces because "," seems to automatically add one (at least in the print function)