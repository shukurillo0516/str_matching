from fuzzywuzzy import fuzz
from fuzzywuzzy import process


TUMANLAR = ["to'rakurg'on", "pop", "uchkurg'on", "namangan", "kosonsoy", "mingbulog'"]


tuman = input("Tuman nomini kiriting: ")

matched_tumanlar = process.extract(tuman.lower(), TUMANLAR, limit=5)

for t in matched_tumanlar:
	# if len(t[0]) == len(tuman):
	print(t) 
	

