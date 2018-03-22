# create table for police neighborhoods
# need to load only once
CREATE TABLE neighborhoods (
	intptlat10 numeric,
	intptlon10 numeric,
	hood text UNIQUE,
	hood_no integer,
	acres numeric,
	sqmiles numeric
	);

# upload police-neighborhoods.csv using "scp police-neighborhoods.csv jiayuz1@sculptor.stat.cmu.edu:~/" then load data
\copy neighborhoods from 'police-neighborhoods.csv' with csv header delimiter as ',';

# check table
SELECT * from neighborhoods where hood_no = 24;

# observation
 intptlat10 | intptlon10  |       hood       | hood_no |  acres  | sqmiles
------------+-------------+------------------+---------+---------+---------
 40.4403871 | -79.9813476 | Crawford-Roberts |      24 | 166.101 |   0.258
(1 row)

# crate table for crime data
# need to update each week 
CREATE TABLE blotter (
    id integer UNIQUE PRIMARY KEY,
    report_name text,
    section text,
    description text,
    arrest_time timestamp without time zone,
    address text,
    neighborhood text,
    zone integer
    );

# add foreign key
ALTER TABLE blotter add FOREIGN KEY (neighborhood) REFERENCES neighborhoods (hood);
