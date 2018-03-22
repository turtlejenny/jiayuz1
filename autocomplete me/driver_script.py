#!/usr/bin/python

import sys
from time import clock
from trie import Node, TrieTree
import autocomplete

# driver script
# one example of command line is like this: python autocomplete.py "the" wiktionary.txt 5
key = sys.argv[1]
filename = sys.argv[2]
K = int(sys.argv[3])

# calculate the time for loading the data and building the tree
start1 = clock()
words = autocomplete.readterms(filename)
end1 = clock()
print("The time for loading the data and building the tree is", end1 - start1)

# calculate the time for finding the matches
start2 = clock()
suggestions = autocomplete.autocomplete(key, words, K)
end2 = clock()
print("The time for finding the matches is", end2 - start2)

# print the results
print("Suggestions are", suggestions)