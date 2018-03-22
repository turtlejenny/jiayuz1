import csv
import sys
import psycopg2
import unittest
import match_data

# test match_data function
class match_test(unittest.TestCase):
	def test1(self):
		conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
		cur = conn.cursor()
		line = "20885,OFFENSE 2.0,3304,Identity Theft,2015-03-10T00:01:00,1400 block Centre Ave,Golden Triangle/Civic Arena,2"
		row = line.split(',')
		self.assertEqual(match_data.matchdata(cur, row), False)

	def test2(self):
		conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
		cur = conn.cursor()
		line = "20885,OFFENSE 2.0,3304,Identity Theft,2015-03-10T00:01:00,1400 block Centre Ave,Squirrel Hill,2"
		row = line.split(',')
		self.assertEqual(match_data.matchdata(cur, row), False)

	def test3(self):
		conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
		cur = conn.cursor()
		line = "20885,OFFENSE 2.0,3304,Identity Theft,2015-03-10T00:01:00,1400 block Centre Ave,Squirrel Hill S,2"
		row = line.split(',')
		self.assertEqual(match_data.matchdata(cur, row), True)

	def test4(self):
		conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
		cur = conn.cursor()
		line = "20885,OFFENSE 2.0,3304,Identity Theft,2015-03-10T00:01:00,1400 block Centre Ave,Squirrel Hill South 2,2"
		row = line.split(',')
		self.assertEqual(match_data.matchdata(cur, row), True)

	def test5(self):
		conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
		cur = conn.cursor()
		line = "20885,OFFENSE 2.0,3304,Identity Theft,2015-03-10T00:01:00,1400 block Centre Ave,Squirrel Hill South,2"
		row = line.split(',')
		self.assertEqual(match_data.matchdata(cur, row), True)

if __name__ == '__main__':
	unittest.main()


