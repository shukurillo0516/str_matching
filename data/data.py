import csv
import os.path
from collections import defaultdict


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PATH = f"{BASE_DIR}/uzbekistan-regions-data/CSV/districts.csv"
PATH_REGIONS = f"{BASE_DIR}/uzbekistan-regions-data/CSV/regions.csv"


def get_regions()-> list:
	data = list()
	with open(PATH_REGIONS) as file:
		f_reader = csv.reader(file)
		for i, row in enumerate(f_reader):
			if i > 0:
				data.append(row)			

	return data


def get_data()-> dict:
	data = defaultdict(list)
	with open(PATH) as file:
		f_reader = csv.reader(file)
		for i, row in enumerate(f_reader):
			# just omiting first line
			if i > 0:
				data[row[1]].extend((row[2], row[3], row[4]))	

	return data


######################## TEST #################################

################## GET REGIONS TEST ##################
# get_regions()


################## GET DATA TEST ##################
# Getting data
data = get_data()

# test_data = list()

# Getting test data
# with open(PATH) as file:
# 		f_reader = csv.reader(file)
# 		for i, row in enumerate(f_reader):
# 			# just omiting first line
# 			if i > 0:
# 				test_data.append(row[2:])	


# Printing data keys
# for  v in data.keys():
# 	print(v)

# Printing test data
# for d in test_data:
# 	print(d) 