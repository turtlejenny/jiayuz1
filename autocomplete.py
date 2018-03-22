#!/usr/bin/python

import queue 
import random
from trie import Node, TrieTree

# define readterms function
# The first line is the number of terms in the file so it need not be loaded.
# For the following lines, which are pairs of terms and weights, separated by tabs,
# split the line into two parts to make them into a dictionary.
def readterms(filename):
	with open(filename, 'r') as f:
		result = {}
		alllines = f.readlines()
		lines = alllines[1:]
		for line in lines:
			line = line.strip()
			result[line.split('\t')[1]] = int(line.split('\t')[0])
		trie = TrieTree(result)
	return(trie)

# define autocomplete function
# Use a priority queue to traverse the nodes with highest weights first, 
# stopping the traversal as soon as having collected k suggestions.
# There are two kinds of nodes, one is the end of a word, which can be categorized as "Word",
# the other doesn't, which can be categorized as "Node".
# For "Word", it has to be pushed into the priority queue twice with the maxweight and its own weight respectively,
# because there's no clue about whether the maxweight comes from itself or its children.
# For "Node", there is no need to be pushed twice.
# First push the current node(the last character of the given key) with maxweight 
# and the default logic value False for whether this node is the end of a word into the priority queue, 
# so as to make sure traversing the nodes with highest weights first.
# If this node is "Word", push it into the queue again but this time with its own weight and logic value True.
# If the node popped from the queue with logic value True, then add the word and the weight into the list respectively.
# If the node popped from the queue with logic value False, look at its children in the similar way.
# As long as the queue isn't empty and there are not enough results, do the same loop.
def autocomplete(key, trie, K): # words is a TrieTree class
	wordlist = []
	weightlist = []
	pq = queue.PriorityQueue()
	try:
		currentnode = trie.search(key)
		pass
	except Exception as e:
		return(list(zip(weightlist, wordlist)))
	currentnode = trie.search(key)
	# define the default logic value to be False
	pq.put((-currentnode.maxweight, random.random(), currentnode, False))
	if currentnode.isword == True:
		# define the logic value to be True
		pq.put((-currentnode.weight, random.random(), currentnode, True))
	
	while len(wordlist) < K and not pq.empty():
		currentnode, deterisword = pq.get()[2:]
		if deterisword == True:
			# its maxweight comes from itself
			wordlist.append(currentnode.word)
			weightlist.append(currentnode.weight)
		else: 
			# look at its children
			for child in currentnode.children: 
				pq.put((-currentnode.children[child].maxweight, random.random(), currentnode.children[child], False))
				if currentnode.children[child].isword == True:
					pq.put((-currentnode.children[child].weight, random.random(), currentnode.children[child], True))	
	
	matches = list(zip(weightlist, wordlist))
	return(matches)
