from s5v2 import *

from prettytable import PrettyTable

def my_table():
  x = PrettyTable(['Style', 'Average Price'])
  x.add_row(['Print', pretty_average(print_ties)])
  x.add_row(['Solid', pretty_average(solid_ties)])
  x.add_row(['Paisley', pretty_average(paisley_ties)])
  x.add_row(['Striped', pretty_average(striped_ties)])
  x.add_row(['Gucci', pretty_average(gucci_ties)])
  print(x)

def pretty_average(my_number):
  pretty_avg = "${:03.2f}".format(find_average(my_number))
  return pretty_avg

#my_table()

def count_prices_for_brands(data_sample, brand, min_price, max_price):
    count = 0
    for row in data_sample: 
        if str(row[0]) == str(brand):
            if min_price < float(row[1]) < max_price: 
              count += 1
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
    tup = build_table_text(data_sample, brand_names)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for group in price_groups:
        plt.bar(group, price_groups[group]) 
    
    if tup[0] and tup[1]:
        ax.table(cellText=tup[0], colLabels=columns, rowLabels=tup[1], loc='bottom')
        ax.text(-1.3, 0, 'Discounted Ties Brands', size=12, horizontalalignment='left', verticalalignment='top')
        ax.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            labelbottom='off') # labels along the bottom edge are off

    fig.savefig(exported_figure_filename, dpi=400, bbox_inches='tight')

from collections import Counter
def group_prices_by_range(prices_in_float):
    
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
  
brands = my_csv['brandName']
columns = ["$0-50", "$50-100", "$100-150", "$150-200", "$200-250", "$250+"]
write_brand_and_price_file("_data/tempTableFile.csv", data_from_csv)
brand_and_price_data = open_with_csv("_data/tempTableFile.csv", d=',')
create_table(brand_and_price_data, price_groups, brands, columns, "_charts/s5_prices_in_table--TEACHER.png")