from s4v3 import * 
from matplotlib.pyplot as plt # import matplotlib's pyplot and assign it to a variable name. I didn't know you could do this, but it's pretty cool for unweildly and long library names or function. However, it's probably not great for universal readability since I'm changing a well known name into a name that I specifically made up
# upon further reflection this "as" statement is seen in the matplotlib.pylot tutorial, so maybe it's more standard

# more on matplotlib.pylot from http://matplotlib.org/users/pyplot_tutorial.html
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., create a figure, create a plotting area in a figure, plot some lines in a plotting area, decorate the plot with labels, etc.... matplotlib.pyplot is stateful, in that it keeps track of the current figure and plotting area, and the plotting functions are directed to the current axes

def create_line_chart(data_sample, title, exported_figure_filename):
	fig = plt.figure() # create a figure object, don't know what this is... but according to the documentation a figure is the "top level container for all plot elements". So it's kinda like a list as it contains all the data that is going to go into our diagram.
	ax = fig.add_subplot(1, 1, 1) # create an axis object within the figure object. This calls the add_subplot function which I'm not familiar with. 

	prices = (sorted(map(float, sample))) # create a variable prices and assign it to the sorted, map (what is a map?), in floats, of the sample... did they mean the data_sample? there is no sample defined... 
	# map(function, iterable, ...) apply the function to every item of iterable. I'm not sure how float is a function... nevermind it's a built in function of python. float() = return a floating point number constructed from a number or a string. ... so, in this case, we are going to apply the float() function to every item in the sample, or sample_data, ... basically map() is going to make every item in the sample (data sample?) a float. Then... what is sorted going to do... I mean, it's probably going to sort them, but how? What's the default sort parameter for sorted()... it doesn't explicitly say, but it seems to be smallest to largest with smallest at the front of the list.

	x_axis_ticks = list(range(len(sample))) # create a variable named x axis ticks (marks?) and assign it the value of the length of the sample (again, data_sample maybe?) as a range as a list? 
	# range() = This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. this is taking the length of the sample as it's arg and it's going to create a list that's the length of the sample. it's not a list of the sample it's simply a list of integers that range from 0 to the len(sample) so something like x = [0, 1, 2, 3, 4, ... len]
	# it looks like list() also just creates a list... 
	# Ok, so here's what I think is happening: we're creating a variable that is the number of increments along the x axis, number of graph markers. It's going to create a list, that's the range, of the length of the data sample, iterating on increments of 1 integer at a time. 

	ax.plot(x_axis_ticks, prices, linewidth=2) # here it looks like we're ploting something on our axis object with the x_axis_ticks, the prices as arguments and with an argument for formatting that sets the graph linewidth to 2)

	ax.set_title(title) # now we're using a function I don't know, probably from the matplotlib that sets the title of the graph. the title arg is pulled from the function args

	ax.set_xlim([0, len(sample)]) # ok, more guess-work here, but it looks like we're setting a limit to the x axis... but really it looks more like a range from 0 to the end of the sample length... the strange thing is that if the sample doesn't increment by one, then the lim might not be right. Like what happens if the sample goes from 10 - 786 but it only has 10 items in the sample. Doesn't len() return the number of items, not the max value? 

	ax.set_xlabel('Tie Price ($)') # finally something straightforward. Set the label of the x axis to Tie Price.

	ax.set_ylabel('Number of Ties') # the label of the y axis

	fig.savefig(exported_figure_filename)

create_line_chart([x[2] for x in gucci_ties] # use list comprehension to iterate through the gucci_ties list and chart the results in this case it looks like we're plotting the values from the third row of the data sample (i.e. x[2]), so basically we're making a list of the values from the third row/column of the data sample, but instead of returning the list or assigning it to a variable we're feeding it directly into the creat line chart function as the data sample ... all of that just for the first function argument. 

# list comprehension ... explained? ... start by placing everything inside the brackets, like the list yo, [].  Then place the thing you wanted to append to the list at the beginning of the statement. then use a for loop to iterate throught the set of values. 

# more at http://www.secnetix.de/olli/Python/list_comprehensions.hawk
