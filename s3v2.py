from s3v1 import *

def filter_col_by_string(data_sample, field, filter_condition):
	filtered_rows = [] # create a new list
	col = int(data_sample[0].index(field)) # create a variable (col) and asign it to an integer which is pulled from the header row of the data_sample and which is the index (probably also an integer to begin with) of the field name that we passed in as an argument
	filtered_rows.append(data_sample[0]) # add the header row to the new list

	for item in data_sample[1:]:
		if item[col] == filter_condition:
			filtered_rows.append(item)

	return filtered_rows

silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
print("Found {} silk ties".format(number_of_records(silk_ties)))