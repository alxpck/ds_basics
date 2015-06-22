from s3v3 import *
import csv

def write_to_file(filename, data_sample):
	example = csv.write(open(filename, 'w', encoding='utf-8'), dialect='excel') # example is the variable of the new file that is open and which we can write to (using utf-8 encoding and an excel dialect). 
	example.writerows(data_sample) # write rows is going to take the rows in the data sample and write them to the example (i.e. the file name we passed in)

write_to_file("_data/s4-silk_ties.csv", silk_ties) # this is going to create a new csv located in the _data directory, named s4-silk_ties.csv and it is going to contain all of that data from the silk_ties list which we created in s3v2 (silk_ties = filter_col_by_string(data_from_csv, "material", "_silk"))

