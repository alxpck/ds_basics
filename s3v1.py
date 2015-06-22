from s2v5 import *

def create_bool_field_from_scratch_term(data_sample, search_term):
	new_array = []
	new_array.append(data_sample[0].append(search_term)) # I'm a little lost on what's going on here. The new (temporary) array is taking the first row of data_sample, i.e. data_sample[0] and adding X (the search term) to the end of the header row
	for row in data_sample[1:]: # for every row in the data set starting after the header row
		new_bool_field = False 
		if search_term in row[7]: # checks to see if X (the search term is in row[7] (the product description row)
			new_bool_field = True # if it is it sets bool to True
		row.append(new_bool_field) # then for each row, regardless of the search term it sets the value to the boolean, but how does it know where to put it? Oh, just on the end. 
		new_array.append(row) # now construct the new_array one row at a time. Before this new_array was just empty (or empty of everything except the new header that included the search term as a new column.
	return new_array # return the new array

def filter_col_by_bool(data_sample, col):
	matches_search_term = [] # create a new list of just the rows that match the search term
	for item in data_sample[1:]: # not sure why we did item instead of row. But we start with the first non-header row in the data sample, and ... maybe item because we're not checking the entire row, we're just checking the item at the column number? Not really sure.
		if item[col]: # if the thing/item/row? at this index point 
			matches_search_term.append(item) # append the item to the new array. in this case it looks like the array is getting the entire row, not just the one cell of the spreadsheet... but again I'm not entirely sure. 
	return matches_search_term

my_new_csv = create_bool_field_from_scratch_term(data_from_csv, "cashmere")

number_of_cashmere_ties = number_of_records(filter_col_by_bool(my_new_csv, 11))

# print("Length:", number_of_cashmere_ties)