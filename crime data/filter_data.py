#!/usr/bin/python

import csv
import sys

# define filterdata function to keep only requried report_name, section and zone
def filterdata(filename):
	with open(filename, 'r') as f:
		next(f)
		# print the result to STDOUT
		wr = csv.writer(sys.stdout, lineterminator='\n')

		sections = set(["3304", "2709", "3502", "13(a)(16)", "13(a)(30)", "3701", "3921", "3921(a)", "3934", "3929", "2701", "2702", "2501"])
		for row in csv.reader(f):
			if row[1] != "ARREST":
				if row[1] is None:
					row[1] = "OFFENSE 2.0"
				if row[7] and row[2] in sections:
					wr.writerow(row)
				else: 
					pass
					
# driver script
filename = sys.argv[1]
filterdata(filename)

