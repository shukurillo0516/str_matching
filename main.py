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
import re
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


def det_alphabet(tuman, data, step):
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

	for i in range(ind, len(data), step):
		res.append(data[i].lower())		
			
	return res, ind


def rectify(u_tuman):
	u_tuman = u_tuman.lower() + " "
	u_tuman = u_tuman.replace(",", " ").replace(" t ", " tumani ").replace(" sh", " shahar ")
	u_tuman = u_tuman.replace(" т ", " тумани ").replace(" ш ", " шаҳри ")
	# Replace viloyat
	u_tuman = u_tuman.replace("viloyati", "").replace("viloyat", "").replace(" v ", "")

	return u_tuman


def extract_tuman(region, u_tuman, ind):
	"""
	This function splits u_tuman, and finds the most matching region adn deletes the region.
	"""
	region_tr, ind = det_alphabet(u_tuman, REGIONS[int(region)-1][1:], 3)

	# dictionary (key index of an item, value is the matching percent)
	values = dict()
	
	#split u_tuman
	arr_tuman = u_tuman.split()
	#loop through item and add index and matching percent to the dict
	temp = int()
	for i, item in enumerate(arr_tuman):
		percent = fuzz.ratio(region_tr[0], item)
		#push only the largest value
		if temp < percent:
			values = {i: percent}
			temp = percent

	#Poping the region
	arr_tuman.pop(list(values)[0])

	#return string
	return " ".join(arr_tuman)


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
	#delete regex patter and handle t and sh
	u_tuman = rectify(u_tuman)
	# Determine alphabet
	data_tumans_tr, ind = det_alphabet(u_tuman, data_tumans, 3)
	# extracting tuman name from string
	e_name =  extract_tuman(region, u_tuman, ind)
	
	matched_tumanlar = process.extract(e_name, data_tumans_tr, limit=5)
	print("########################## RESULT #################################")
	print(matched_tumanlar)
	print("###########################################################")
	print()


while True:
	main()
