#!usr/bin/python

import random

# generate a random subset from the original text file
def randomsubset(filename, textname):
	with open(filename, 'r') as f:
		alllines = f.readlines()
		lines = random.sample(alllines[1:], 50)

	with open(textname,'w') as f:
		for line in lines:
			strline= str(line)
			f.write(strline)

# read the ramdom subset
def readrandom(filename):
	with open(filename, 'r') as f:
		result = {}
		alllines = f.readlines()
		lines = alllines[1:]
		for line in lines:
			line = line.strip()
			result[line.split('\t')[1]] = int(line.split('\t')[0])
		return(result)

# manually search the prefix to find the most highest K suggestions
def checkrandom(key, filename, K):
	wordlist = []
	weightlist = []
	for string, weight in filename.items():
		if string.startswith(key) == True:
			wordlist.append(string)
			weightlist.append(weight)
		else:
			pass
	matches = list(zip(weightlist, wordlist))
	final = sorted(matches, reverse=True)
	return(final[:K])