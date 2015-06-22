from s4v1 import *

def write_brand_and_price_file(filename, data_sample):
	brand_field_index = 5
	price_field_index = 2
	new_array = []
	for record in data_sample:
		new_record = [None] * 2 # create two empty elements in the new_array for each record, not sure why we're doing this. It seems like we're filling it with null placeholders. Couldn't we just populate the array with the actual data? What's the point in placeholding two empty elements in the array? I guess we're just getting really explict about what we want?
		new_record[0] = record[brand_field_index] # the first element is the brand
		new_record[1] = record[price_field_index] # the second element is the price
		new_array.append(new_record) # append the new record to the new array
	write_to_file(filename, new_array) # instead of returning the values we're going to reuse the write to file function and return the new array as the data set for the new file. I guess this makes sense as the write brand and price file function is wants to write a file not return vales. The other way to do this would be to write out all of the write to file function as the end of the write brand and price file function, but DRY says to just reuse the function.

write_brand_and_price_file('_data/s4-brand_and_price.csv', gucci_ties)

def write_min_max_csv(filename, data_sample):
	min = find_max_min(data_sample, 2, "min") # use the data sample, look in column 2, and get the min value and assign it to the variable min
	max = find_max_min(data_sample, 2, "max") # use the data sample, look in column 2, and get the max value and assign it to the variable max
	new_array = [] # create a new empty list
	for record in data_sample: 
		if (float(record[2]) == min) or (float(record[2]) == max): # if the float of the record equals either the min value (in the min variable) or the max value (in the max variable) then... 
			new_array.append(record) # append that record to the new array list
	write_to_file(filename, new_array) # reuse that write to file function again

write_min_max_csv('_data/s4-min_max_csv', gucci_ties[1:]) # this time we're skipping over the the header row, because we're not using the header label to choose the column index (because we hard coded the column index, 2, in the function). 

