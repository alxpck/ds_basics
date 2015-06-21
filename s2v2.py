from s2v1 import *

def number_of_records(data_sample):
	return len(data_sample)

number_of_ties = number_of_records(data_from_csv)

print(number_of_ties, "ties in our data sample")