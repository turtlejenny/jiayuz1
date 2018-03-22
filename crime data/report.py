#!/usr/bin/python

import sys
import psycopg2
import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates

conn = psycopg2.connect(host="sculptor.stat.cmu.edu", database="jiayuz1",
                        user="jiayuz1", password="52737186")
cur = conn.cursor()

# produce a table of counts of crimes each week, split up by type of crime
cur.execute("""SELECT section as section, description as crime_type, count(*) as count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time)<=7
	group by section, crime_type order by count""")

header1 = ["Section", "Crime Type", "Counts of Crimes"]
alldata = []
for row in cur:
    alldata.append(row)
print("Crime Counts Each Week by Type of Crime:", file = open("weekly_report.txt", 'a'))  
print("\n" + tabulate.tabulate(alldata, header1), file = open("weekly_report.txt", 'a'))

# Graph the total number of crimes per day over the past month
cur.execute("""SELECT arrest_time::date as day, count(*) as count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time)<=30
	group by day order by day""")

# list the changes in number of crimes between this week and last week
# split up by police zone
cur.execute("""SELECT this_week.zone as this_zone, last_week.zone as last_zone,
	this_week.this_week_count as this_count, last_week.last_week_count as last_count into temp1 from
	(SELECT zone, count(*) as this_week_count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time)<=7
	group by zone) this_week
	FULL OUTER JOIN
	(SELECT zone, count(*) as last_week_count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time) between 7 and 14
	group by zone) last_week
	on this_week.zone = last_week.zone
	order by this_week.zone""")
cur.execute("""UPDATE temp1 set this_zone=last_zone, this_count=0 where this_zone is NULL""")
cur.execute("""UPDATE temp1 set last_zone=this_zone, last_count=0 where last_zone is NULL""")
cur.execute("""SELECT this_zone as zone, this_count-last_count as change from temp1 order by zone""")

header2 = ["Police Zone", "Changes in Number of Crimes \n (this week - last week)"]
zonedata = []
for row in cur:
    zonedata.append(row)   
print("\nChanges in Number of Crimes Between This Week and Last Week by Police Zone:", file=open("weekly_report.txt", 'a'))    
print('\n' + tabulate.tabulate(zonedata, header2), file=open("weekly_report.txt", 'a'))

# split up by neighborhood
cur.execute("""SELECT this_week.neighborhood as this_neighborhood, last_week.neighborhood as last_neighborhood,
	this_week.this_week_count as this_count, last_week.last_week_count as last_count into temp2 from
	(SELECT neighborhood, count(*) as this_week_count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time)<=7
	group by neighborhood) this_week
	FULL OUTER JOIN
	(SELECT neighborhood, count(*) as last_week_count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time) between 7 and 14
	group by neighborhood) last_week
	on this_week.neighborhood = last_week.neighborhood
	order by this_week.neighborhood""")
cur.execute("""UPDATE temp2 set this_neighborhood=last_neighborhood, this_count=0 where this_neighborhood is NULL""")
cur.execute("""UPDATE temp2 set last_neighborhood=this_neighborhood, last_count=0 where last_neighborhood is NULL""")
cur.execute("""SELECT this_neighborhood as neighborhood, this_count-last_count as change from temp2 order by neighborhood""")

header3 = ["Neighborhood", "Changes in Number of Crimes \n (this week - last week)"]
neighborhooddata = []
for row in cur:
    neighborhooddata.append(row)   
print("\nChanges in Number of Crimes Between This Week and Last Week by Neighborhood:", file=open("weekly_report.txt", 'a'))    
print('\n' + tabulate.tabulate(neighborhooddata, header3), file=open("weekly_report.txt", 'a'))

# Graph the total number of crimes per day over the past month
cur.execute("""SELECT arrest_time::date as day, count(*) as count from blotter 
	where date_part('day', (SELECT max(arrest_time) from blotter)-arrest_time)<=30
	group by day order by day""")

date = []
frequency = []
for row in cur:
    date.append(row[0])
    frequency.append(row[1])
plt.title("Crime Counts Per Day Over the Past Month")
plt.xlabel("Date")
plt.ylabel("Frequency")
plt.grid(True)
plt.bar(date, frequency, align="center")
plt.xticks(date, rotation=90)
formatter = matplotlib.dates.DateFormatter("%y/%m/%d")
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.subplots_adjust(left=0.07, right=0.98, bottom=0.2)
plt.show()