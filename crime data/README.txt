Filter Data:
When filtering the data read from CSV file, 
I have only included OFFENSE 2.0 reports of the types indicated in Table1 and skipping crimes with no zone,
using if clause to check whether repore_name is OFFENSE 2.0, 
whether the section is in list 
["3304", "2709", "3502", "13(a)(16)", "13(a)(30)", "3701", "3921", "3921(a)", "3934", "3929", "2701", "2702", "2501"],
and whether the zone is NULL. 
Then print the result as a CSV to STDOUT.

Ingest Data:
When ingesting the data read from STDIN, there are two things I need to implement.
The first one is changing the element type and matching the neighborhood names.
This procedure is also required in patching data, so I have defined a function here.
Since I have stated the type of each column in "blotter", 
id, arrest_time and zone should be converted into interger, timestamp and integer respectively.
As for matching the neighborhood names, there are several cases I should take into consideration.
If the original neighborhood in "blotter" is the correct hood in "neighborhoods",
then no work is needed to be done and return the Boolean logic value True.
If the original neighborhood in "blotter" is a substring of the correct hood in "neighborhoods",
then replace it with the corresponding correct hood and return the Boolean logic value True.
If the original neighborhood in "blotter" is contains the correct hood in "neighborhoods",
then replace it with the corresponding correct hood.
If there are multiple different matches,
then log error message and return the Boolean logic value False.
If no correct hood in "neighborhoods" could be found for original neighborhood in "blotter", 
then log error message and return the Boolean logic value False.
The second one is inserting those matched records into "blotter" and catch potential errors.
Try insert each record into "blotter" except error.
If the error code is "23505", which means unique_violation in psql, then log error message.
If there are other expected errors, then log error message.

Patch Data:
When patching data, there are two things I need to implement.
The first one is the same with ingesting data.
The second one is updating older records with new records for a duplicated id in "blotter", inserting new records into "blotter"
and catch potential errors.
Try insert each record into "blotter" except error.
If the error code is "23505", which means unique_violation in psql, then update that record with the new patch record.
If there are other expected errors, then log error message.

The command lines are listed below in order:
$ py filter_data.py crime-base.csv | py ingest_data.py
$ py filter_data.py crime-week-1.csv | py ingest_data.py
$ py filter_data.py crime-week-1-patch.csv | py patch_data.py
$ py filter_data.py crime-week-2.csv | py ingest_data.py
$ py filter_data.py crime-week-2-patch.csv | py patch_data.py
$ py filter_data.py crime-week-3.csv | py ingest_data.py
$ py filter_data.py crime-week-3-patch.csv | py patch_data.py
$ py filter_data.py crime-week-4.csv | py ingest_data.py
$ py filter_data.py crime-week-4-patch.csv | py patch_data.py
$ py report.py