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

def build_table_text(data_sample, brands):  
	cell_text = []
	row_text = []  
	unique_brand_list = sorted(set(brands))
	for b in unique_brand_list: 
		b = bytes.decode(b)
		temp_row = [] 
		group1 = count_prices_for_brands(data_sample, b, 0, 50.00)
		group2 = count_prices_for_brands(data_sample, b, 50.00, 100.00)
		group3 = count_prices_for_brands(data_sample, b, 100.00, 150.00)
		group4 = count_prices_for_brands(data_sample, b, 150.00, 200.00)
		group5 = count_prices_for_brands(data_sample, b, 200.00, 250.00)
		group6 = count_prices_for_brands(data_sample, b, 250.00, 1000.00)
		row_list = [group1, group2, group3, group4, group5, group6]
		temp_row.extend(row_list) 

		if group1 > 0:
			if any([x >= group1 for x in row_list[1:]]):
				cell_text.append(temp_row)
				row_text.append(b)
	return (cell_text, row_text)

def create_table(data_sample, price_groups, brand_names, columns, exported_figure_filename):
	tup = build_table_text(data_sample, brand_names) # create a tuple of the table text using the brand names
	fig = plt.figure() # create a figure object
	ax = fig.add_subplot(1, 1, 1) # create an axis object

	for group in price_groups: # iterate through the price groups
		plt.bar(group, price_groups[group]) # create a bar for each price group

	if tup[0] and tup[1]: # check that the tuple has two values, if so... 
		ax.table(cellText=tup[0], colLabels=columns, rowLabels=tup[1], loc='bottom') # use the first value as the cell text, use teh second value as the row label and create a table on the axis object
		ax.text(-1.3, 0, 'Discounted Ties Brands', size=12, horizontalalignment='left', verticalalignment='top') # create text on the axis object, hard-coded inputs
		ax.tick_params(
			axis='x',          # changes apply to the x-axis
			which='both',      # both major and minor ticks are affected
			labelbottom='off') # labels along the bottom edge are off
			# set the ticks for the axis, this is all visual formatting
	fig.savefig(exported_figure_filename, dpi=400, bbox_inches='tight') # save the newly created figure 

from collections import Counter
def group_prices_by_range(prices_in_float): # we used this function in a previous lesson. It helps us sort prices into rough categories/buckets/ranges so that our bar chart is easier to read. 

	tally = Counter()

	for item in prices_in_float:
		bucket = 0
		rounded_price = round(item, -1)
		if 0 <= rounded_price <= 50:
			bucket = 1
		elif 50 <= rounded_price <= 100:
			bucket = 2
		elif 100 <= rounded_price <= 150:
			bucket = 3
		elif 150 <= rounded_price <= 200:
			bucket = 4
		elif 200 <= rounded_price <= 250:
			bucket = 5
		elif 250 <= rounded_price:
			bucket = 6
		else:
			bucket = 7

		tally[bucket] += 1
	return tally

price_groups = group_prices_by_range(price_in_float)
brands = my_csv['brandName']
columns = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
write_brand_and_price_file("_data/tempTableFile.csv", data_from_csv)
brand_and_price_data = open_with_csv("_data/tempTableFile.csv", d=',')
create_table(brand_and_price_data, price_groups, brands, columns, "_charts/prices_in_table.png")
