#!/usr/bin/python

import csv
import sys
import psycopg2
import match_data

# replace old data and add new data
num = 0
conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
cur = conn.cursor()

# convert unmatched types
for line in sys.stdin.readlines():
	row = line.split(",")

	# rematch the unmatched neighborhoods
	match = match_data.matchdata(cur, row)

	if match is True:
		num +=1
		try:
			cur.execute("""INSERT into blotter (id, report_name, section, description, arrest_time, address, neighborhood, zone) 
							values (%s, %s, %s, %s, %s, %s, %s, %s)""", (row))
			conn.commit()
		except Exception as error:
			conn.rollback()
			# replace old data
			if error.pgcode == "23505":
				print("updated id:", str(row), file=open("patch records.txt", 'a'))
				cur.execute("""UPDATE blotter set report_name=%s, section=%s, description=%s, arrest_time=%s,
						address=%s, neighborhood=%s, zone=%s where id=%s""", (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]))
				conn.commit()
				# catch other errors
			else:
				print("other errors:", str(row), file=open("patch_errors.txt", 'a'))

print("patched records:", num, file=open("patch_records.txt", 'a'))
conn.commit()
conn.close()