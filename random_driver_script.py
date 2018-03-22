#!usr/bin/python

import random
import sys
from trie import Node, TrieTree
import autocomplete

# driver script
# one example of command line is like this: python autocomplete.py "the" wiktionary.txt 5
key = sys.argv[1]
filename = sys.argv[2]
K = int(sys.argv[3])

words = random_test.readterms(filename)


# calculate the time for finding the matches
suggestions = autocomplete.autocomplete(key, words, K)

# print the results
print("Suggestions are", suggestions)

def random_readterms(filename):
	with open(filename, 'r') as f:
		result = {}
		alllines = f.readlines()
		lines = random.sample(alllines[1:], 10)
		for line in lines:
			line = line.strip()
			result[line.split('\t')[1]] = int(line.split('\t')[0])
		trie = TrieTree(result)
	print(result)
	return(trie)

# random test for autocomplete
words = random_readterms("wkitionary.txt")
autocomplete("the", )


