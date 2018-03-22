
import unittest
import autocomplete
import randomcheck
from trie import TrieTree, Node

# test TrieTree.add
class TrieTree_add_test(unittest.TestCase):
	def test_add1(self):
		dic = {'to': 9}
		T = TrieTree(dic)
		T.add('the', 6)
		self.assertEqual(T.trie.children['t'].maxweight, 9)
		self.assertEqual(T.trie.children['t'].isword, False)
		self.assertEqual(T.trie.children['t'].children['o'].weight, 9)
		self.assertEqual(T.trie.children['t'].children['o'].word, 'to')
		self.assertEqual(T.trie.children['t'].children['o'].isword, True)
		self.assertEqual(T.trie.children['t'].children['h'].maxweight, 6)
		self.assertEqual(T.trie.children['t'].children['h'].children['e'].weight, 6)		
		T.add('them', 10)
		self.assertEqual(T.trie.children['t'].maxweight, 10)
		self.assertEqual(T.trie.children['t'].children['h'].isword, False)
		self.assertEqual(T.trie.children['t'].children['h'].maxweight, 10)
		self.assertEqual(T.trie.children['t'].children['h'].children['e'].weight, 6)
		self.assertEqual(T.trie.children['t'].children['h'].children['e'].maxweight, 10)
		self.assertEqual(T.trie.children['t'].children['h'].children['e'].children['m'].weight, 10)
		self.assertEqual(T.trie.children['t'].children['h'].children['e'].children['m'].word, "them")


# test TrieTree.serach:
class TrieTree_search_test(unittest.TestCase):
	def test_search1(self):
		dic = {'to': 5, 'them': 9, 'too': 8, 'the': 7}
		T = TrieTree(dic)
		self.assertEqual(T.search('the').weight, 7)
		self.assertEqual(T.search('the').maxweight, 9)
		self.assertEqual(T.search('to').weight, 5)
		self.assertEqual(T.search('to').maxweight, 8)
		self.assertEqual(T.search('too').weight, 8)
		self.assertRaises(ValueError, lambda: T.search('te'))

# test autocomplete function:
class autocomplete_test(unittest.TestCase):
	def test_autocomplete1(self):
		dic = {'to': 5, 'them': 9, 'too': 8, 'the': 7, 'there': 10, 'took': 6}
		words = TrieTree(dic)
		self.assertEqual(autocomplete.autocomplete('the', words, 2), [(10, 'there'), (9, 'them')])
		self.assertEqual(autocomplete.autocomplete('to', words, 2), [(8, 'too'), (6, 'took')])
		self.assertEqual(autocomplete.autocomplete('too', words, 2), [(8, 'too'), (6, 'took')])
		self.assertEqual(autocomplete.autocomplete('tho', words, 2), [])
	def test_autocomplete2(self):
		words = autocomplete.readterms("wiktionary.txt")
		self.assertEqual(autocomplete.autocomplete('the', words, 5), [(5627187200, 'the'), (334039800, 'they'), (282026500, 'their'), (250991700, 'them'), (196120000, 'there')])

# random test
class random_test(unittest.TestCase):
	def test1(self):
		randomcheck.randomsubset("wiktionary.txt", "random.txt")
		trie1 = randomcheck.readrandom("random.txt")
		trie2 = autocomplete.readterms("random.txt")
		self.assertEqual(autocomplete.autocomplete('t', trie2, 2), randomcheck.checkrandom('t', trie1, 2))
		self.assertEqual(autocomplete.autocomplete('au', trie2, 2), randomcheck.checkrandom('au', trie1, 2))

if __name__ == '__main__':
   unittest.main()
