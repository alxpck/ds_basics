from s2v2 import * 

def calculate_sum(data_sample):
	total = 0
	for row in data_sample[1:]: # slice to start at row two, but I think we should only skip row 1 if we're importing the full csv (data_from_csv), but if we use the data w/ the header (my_csv) we'll be skipping a row that we're not supposed to skip (the actual first row of non-header data). 
		price = float(row[2])
		total += price
	return total

print('the sum total of prices for all ties in the dataset = ' + str(calculate_sum(data_from_csv))) # ok we're using the right import, but having two imports is confusing. 