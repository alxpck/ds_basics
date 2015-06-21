import csv

# needed for following along at home
import numpy

# needed for following along at home
d = '\t'

def open_with_csv(filename, d='\t'):
	data = []
	with open(filename,  encoding='utf-8') as tsvin:
		tie_reader = csv.reader(tsvin, delimiter='\t')
		for line in tie_reader:
			data.append(line)
	return data

data_from_csv = open_with_csv('data.csv')
# print(data_from_csv[0])

# output of the print funtion above
FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'patterned', 'material']

# where did this come from?
# should there be a comma after the last tuple?
DATATYPES = [
	('myint', 'i'),
	('myid', 'i'),
	('price', 'f8'),
	('name', 'a200'),
	('brandId', '<i8'),
	('brandname', 'a200'),
	('imageUrl', '|S500'),
	('description', '|S900'),
	('vendor', '|S100'),
	('pattern', '|S50'),
	('material', '|S50')
]

# use built-in function of NumPy
def load_data(filename):
	my_csv = numpy.genfromtxt(filename, delimiter=d, skip_header=1, invalid_raise=False, names=FIELDNAMES, dtype=DATATYPES)
	return my_csv

my_csv = load_data('data.csv')