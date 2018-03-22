#!/usr/bin/python

# define Node class
# Define a Node class to store its word, its own weight, the maxweight,
# whether the node is the end of a word and its child node.
class Node(object):
	def __init__(self, word=None, weight=None, maxweight=float("-inf")):
		self.word = word
		self.weight = weight
		self.maxweight = maxweight
		self.isword = False
		self.children = {}

# define TrieTree class
# TrieTree.add inserts the word and weight into the trie, updates the maxweight 
# and assigns the Boolean logic value of whether the node is the end of a word.
# TrieTree.search determines whether a given prefix exists in the trie. 
# If it is, then find the node of the last charater.
class TrieTree(object):
    def __init__(self, words): # words is a dictionary
        self.trie = Node()
        for word, weight in words.items():
            self.add(word, weight)  

    # build tree with maxweight
    def add(self, word, weight): # word, weight are from the dictionary
        tree = self.trie
        for char in word:
        	# update the maxweight on the way
        	if weight > tree.maxweight:
        		tree.maxweight = weight    	
        	if char in tree.children:
        		tree = tree.children[char]
        	else:
        		# create a new node
        		tree.children[char] = Node()
        		tree = tree.children[char]
        tree.word = word
        tree.weight = weight
        tree.isword = True
    
    # search the prefix to determine if it exists in the tree
    def search(self, prefix):
        currentnode = self.trie
        for char in prefix:
        	if char in currentnode.children:
        		currentnode = currentnode.children[char]
        	else:
        		raise ValueError('prefix not in the tree')
        return(currentnode)

