from s3v1 import *

def filter_col_by_string(data_sample, field, filter_condition):
	filtered_rows = [] # create a new list
	col = int(data_sample[0].index(field)) # create a variable (col) and asign it to an integer which is pulled from the header row of the data_sample and which is the index (probably also an integer to begin with) of the field name that we passed in as an argument
	filtered_rows.append(data_sample[0]) # add the header row to the new list

	for item in data_sample[1:]:
		if item[col] == filter_condition:
			filtered_rows.append(item)

	return filtered_rows

def filter_col_by_float(data_sample, field, direction, filter_condition):
	filtered_rows = []
	col = int(data_sample[0].index(field)) # you must use integers to access indexes. So this is just to be sure it's not a float or a string.
	cond = float(filter_condition)

	for row in data_sample[1:]:
		element = float(row[col])

		if direction == "<"
			if element < cond:
				filtered_rows.append(row)
		elif direction == "<="
			if element <= cond:
				filtered_rows.append(row)
		elif direction == ">"
			if element > cond:
				filtered_rows.append(row)
		elif direction == ">="
			if element >= cond:
				filtered_rows.append(row)
		elif direction == "=="
			if element == cond:
				filtered_rows.append(row)
		else:
			pass # the pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action. 
	return filtered_rows


silk_ties = filter_col_by_string(data_from_csv, "material", "_silk")
wool_ties = filter_col_by_string(data_from_csv, "material", "_wool")
cotton_ties = filter_col_by_string(data_from_csv, "material", "_cotton")
gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci") # this search term is case sensitive. It came back with 1 tie when I used "gucci" and 171 ties when I used "Gucci" I went to look for the one tie with lowercase gucci in the dataset (manual search), but it didn't come up. What's going on with the 1 "gucci" tie?
falfkafj_ties = filter_col_by_string(data_from_csv, "brandName", "falfkafj") # this a test of a non-existant thing to see if the lowercase "gucci" tie was a global error... like every request will return a minimum of one record even if zero exist. 


# print("Found {} silk ties".format(number_of_records(silk_ties)))
# print("Found {} wool ties".format(number_of_records(wool_ties)))
# print("Found {} cotton ties".format(number_of_records(cotton_ties)))
# print("Found {} Gucci ties".format(number_of_records(gucci_ties)))
# print("Found {} falfkafj ties".format(number_of_records(falfkafj_ties)))


