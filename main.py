"""
	This is project made to find the best matching tuman to the given input.

	Tasks TODO:
		1. Data Loading
		  	Done 1. Load data from csv file
			Done 2. Make a dict with key of regions and data of the districts
		2. Getting user's input
			Done 0. Determining region
			Done 1. Get user's raw input
			Done 2. Lower the case
			Done 3. Determine the alphabet
			Done 4. Path the user's input to matching func with appropriate data
"""
import string

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from data.data import get_data, get_regions


REGIONS  = get_regions()
DATA = get_data()
E_LETTERS = string.ascii_lowercase

def get_region():
	global REGIONS
	"""
	First prints all the regions with id
	"""
	for region in REGIONS:
		print(f"id: {region[0]}, Name: {region[1]}", end=" # ")

	print("")
	try:
		region = input("Enter region id: ")	
	except TypeError:
		print("Only integers can be entered")

	return region


def det_alphabet(tuman, data):
	"""
	This func takes word, and tumans
	Checks the alphabet if the alphabet is cyrilic, returns list of cyrilic names
	"""
	global E_LETTERS 	
	ind = 1
	res = list()

	for l in E_LETTERS:
		if l in tuman:
			ind = 0
			break

	for i in range(ind, len(data), 3):
		res.append(data[i])		
			
	return res


def main():
	global DATA
	"""
	This function calls get_region funct for the region,
	then gets tuman's name,
	then determines alphabet,
	then displays 5 the best matching tumans
	"""
	# Getting region
	region = get_region()
	# Getting tumans
	data_tumans = DATA[region]
	# Getting user tuman
	u_tuman = input("Enter name of tuman: ").lower()
	# Determine alphabet
	data_tumans_tr = det_alphabet(u_tuman, data_tumans)
	matched_tumanlar = process.extract(u_tuman, data_tumans_tr, limit=5)
	print(matched_tumanlar)


main()
