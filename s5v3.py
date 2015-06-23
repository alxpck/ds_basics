from s5v2 import *
from prettytable import PrettyTable

def my_table(): # no arguments are passed in, which seems a bit weird. We're hard-coding a function that only does one thing.
	x = PrettyTable(['Style', 'Average Price']) # setup a new pretty table list and give and give it two list items
	x.add_row(['Print', pretty_average(print_ties)]) # add_row is a built-in function of prettytable. We're going to add a row and assign it the vales of 'Print' and the average price of all print ties
	x.add_row(['Solid', pretty_average(solid_ties)])
	x.add_row(['Paisley', pretty_average(paisley_ties)])
	x.add_row(['Striped', pretty_average(striped_ties)])
	x.add_row(['Gucci', pretty_average(gucci_ties)])
	print(x) # print the table

def pretty_average(my_number):
	pretty_avg = "${:03.2f}".format(find_average(my_number)) # assign a variable pretty_avg to the average of my number and then use the format specification mini-language to add three decimal places before the decimal point and 2 after the decimal point. the FSML says that 'f' is a fixed point and displays the number as a fixed-point number. That's like floating point number, but with a fixed amount of float? As far as what kind of variable it is (string, integer, float / decimal) it's still a decimal or float, just a fixed amount of float. See I was calling this string formatting, but really it's format specification mini-language and it doesn't automatically convert the result to a string (like I originally thought). 
	return pretty_avg

# my_table() # run the function

def count_prices_for_brands(data_sample, brand, min_price, max_price): # overall this function should let us enter a dataset, a brand name, and a price range min-max and then give us a count of how many ties fit these criteria in the data sample
	count = 0 # initialize a counter variable at 0
	for row in data_sample: # loop through the data
		if str(row[0]) == str(brand): # check to see if a  string in the header row is equal to the string of the brand (name) variable, ... actually this is a bit confusing. I think it's going to check the whole first row of the data sample (the header row), but I don't know what the brand argument is going to be if what we were really doing was checking the string of row[4] (column 4, i.e. brand name) then it would make more sense because we'd be checking to see if the row contained a brand we cared about, as is now I'm not sure what we're doing...  
			if min_price < float(row[1]) < max_price: # check to see if the float of the value in row/column 1 (the price column is greater than the min_price we care about (entered as an arg) and less than the max_price we care about (entered as an arg) ... if so ... 
				count += 1 # incriment the count by one
	return count