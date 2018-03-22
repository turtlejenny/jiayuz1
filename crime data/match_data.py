#!/usr/bin/python

import csv
import sys
import psycopg2

# define matchdata function to match the correct names
def matchdata(cur, row):
	cur.execute("""SELECT hood from neighborhoods""")
	allhoods = [hood[0] for hood in cur.fetchall()]
	match = True

	# convert unmatched types
	row[0] = int(row[0])
	row[4] = row[4].replace("T", " ")
	row[7] = int(row[7])

	if row[6] not in allhoods:
		# find neighborhoods containing a certain string
		cur.execute("""SELECT hood from neighborhoods where lower(hood) ilike '%%%s%%'""" %row[6])
		sub = [hood[0] for hood in cur.fetchall()]
		# find neighbhorhoods which are a substring of a certain string
		cur.execute("""SELECT hood from neighborhoods where '%s' ilike format('%%%%%%s%%%%', lower(hood))""" %row[6])
		contain = [hood[0] for hood in cur.fetchall()]
		
		if len(sub) != 0 or len(contain) != 0:
			if len(sub) == 1:
				print(str(row), ": has be replaced with correct name", sub[0], file=open("neighborhood_matches.txt", 'a'))
				row[6] = sub[0]
			elif len(contain) == 1:
				row[6] = contain[0]
				print(str(row), ": has be replaced with correct name", contain[0], file=open("neighborhood_matches.txt", 'a'))
			else:
				match = False
				print(str(row), ": could not match any neighborhood", file=open("neighborhood_errors.txt", 'a'))
		else:
			match = False
			print(str(row), ": could not match any neighborhood", file=open("neighborhood_errors.txt", 'a'))
	return(match)