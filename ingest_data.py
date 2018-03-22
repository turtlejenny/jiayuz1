#!/usr/bin/python

import csv
import sys
import psycopg2
import match_data

# drop the duplicated records, match the neighborhood names and catch other errors
conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
cur = conn.cursor()

for line in sys.stdin.readlines():
	row = line.split(",")

	# rematch the unmatched neighborhoods
	match = match_data.matchdata(cur, row)

	if match is True:
		try:
			cur.execute("""INSERT into blotter (id, report_name, section, description, arrest_time, address, neighborhood, zone) 
							values (%s, %s, %s, %s, %s, %s, %s, %s)""", (row))
			conn.commit()
		except Exception as error:
			conn.rollback()
			# catch duplicated id errors
			if error.pgcode == "23505":
				print("duplicated id:", str(row), file=open("ingest_errors.txt", 'a'))
			# catch other errors
			else:
				print("other errors:", str(row), file=open("ingest_errors.txt", 'a'))

conn.commit()
conn.close()