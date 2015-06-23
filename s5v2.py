from s5v1 import *

def plot_all_bars(price_in_float, exported_figure_filename):
	prices = list(map(int, price_in_float)) # create a list of prices, maping the int() function onto each item in the price in float list
	X = numpy.arange(len(prices)) # use numpy to arange (how?) the length of the prices variable, and then assign it all to a variable named X
	width = 0.25 # guess-work, but I think this means that we're setting the width of the bar plot to 0.25 (inches?). I'm guessing this is just a formatting variable that we'll reuse later.
	plt.xlim([0,5055]) # we're setting the x limit here as a range from 0 = 5055, right?
	plt.savefig(exported_figure_filename) # save the figure (graphic)

def create_bar_chart(price_groups, exported_figure_filename):
	fig = plt.figure() # create a figure object
	ax = fig.add_subplot(1,1,1) # create an axis object and set it to 1 x 1 y and 1 z
	plt.style.use('ggplot') # add a stylesheet for the colors
	colors = plt.rcParams['axes.color_cycle'] # just no idea about this beyond the fact that we're setting a color variable and rcParams is probably formatting function of matplotlib or pyplot. cycle means cycle through the available colors

	for group in price_groups:
		ax.bar(group, price_groups[group], color=colors[group%len(price_groups)]) # this is the thing that creates the bar. It uses the group data, the price from the price groups for that group, and the color assigned to the group
		labels = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"] # a list of labels, one for each range of prices
		ax.legend(labels) # it looks like the legend() function is what you use to label the graph and we're passing in the labels list

		ax.set_title("Amount of Ties at price points") # set the graph title

		ax.set_xlabel("Tie Price ($)") # label the x axis
		ax.set_xticklabels(labels, ha='left')
		ax.set_xticks(range(1, len(price_groups)+1)) # we're setting the markers on the edge of the graph, and we're setting them to the range of 1-length. The +1 is there because len returns a value that starts counting at 0 and, in this case, we want to start counting from 1, so we need to move evenything up by 1

		ax.set_ylabel("Number of Ties") # label the y axis

		plt.grid(True) # Yeah, it's a grid or something
		fig.savefig(exported_figure_filename) # save that graph


from collections import Counter # shouldn't this be at the top of the file?

def group_prices_by_range(price_in_float):
	tally = Counter() # the counter object will count our number of objects

	for item in price_in_float: # loop through the prices and put them into buckets depending on their price
		bucket = 0
		rounded_price = round(item, -1) # round the price of the item ... but what's the -1 for? are we forcing it to round down? ... from the documentation ... round(number, ndigits) = Return the floating point value number rounded to ndigits digits after the decimal point. If ndigits is omitted, it defaults to zero. ... so we're rounding to -1 digits after the decimal which seems like we're really saying round to the ones place (i.e. 9.99 rounds to 10) how is this different from rounding to the 0 ndigits? 
		# Values are rounded to the closest multiple of 10 to the power minus ndigits; if two multiples are equally close, rounding is done away from 0 (so, for example, round(0.5) is 1.0 and round(-0.5) is -1.0).
		if rounded_price >= 0 and rounded_price <= 50:
			bucket = 1
		elif rounded_price >= 50 and rounded_price <= 100:
			bucket = 2
		elif rounded_price >= 100 and rounded_price <= 150:
			bucket = 3
		elif rounded_price >= 150 and rounded_price <= 200:
			bucket = 4
		elif rounded_price >= 200 and rounded_price <= 250:
			bucket = 5
		elif rounded_price >= 250:
			bucket = 6
		else:
			bucket = 7

		tally[bucket] += 1

	return tally

price_groups = group_prices_by_range(price_in_float)
create_bar_chart(price_groups, "_charts/s5-price_in_groups.png")

