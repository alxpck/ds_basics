from s2v2 import * 

def calculate_sum(data_sample):
	total = 0
	for row in data_sample[1:]: # slice to start at row two, but I think we should only skip row 1 if we're importing the full csv (data_from_csv), but if we use the data w/ the header (my_csv) we'll be skipping a row that we're not supposed to skip (the actual first row of non-header data). 
		price = float(row[2]) # I would think of this as column[2], not sure why it's row[2]. 
		total += price
	return total


def calculate_sum_succinct(data_sample):
	prices = [float(row[2]) for row in data_sample[1:]]
	return sum(prices)

# Personally, I would abstract this more. I'd make this function return the list of prices and then have a second function that just did the sum of it, or let myself just add the built in sum() function.
def list_of_prices(data_sample):
	prices = [float(row[2]) for row in data_sample[1:]]
	return prices

# print('the sum total of prices for all ties in the dataset = ',  calculate_sum(data_from_csv)) # ok we're using the right import, but having two imports is confusing. UPDDATE: No, I don't have to convert the calculate_sum result to a string to add text about it, I just need to use , instead of +

# print(calculate_sum_succinct(data_from_csv))

# print(sum(list_of_prices(data_from_csv)))