
# a trie node that stores its value, whether it represents the end of the 
# word, and the node's children
class TrieNode:
	def __init__(self, val, endOfWord=False):
		self.children = {}
		self.val = val
		self.endOfWord = endOfWord


class Trie:
	def __init__(self, val=None, endOfWord=False):
		self.root = TrieNode(val, endOfWord)
		self.levels = 0

	# def __str__(self):
	# 	level = 0

	# 	pass


    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    def insert(self, word):
    node = self.root
    for c in word:
        next_node = node.children.get(c, None)

        # this character at this level doesn't exist, we need to create it
        if next_node is None:
            next_node = TrieNode(c)

            # add it to node's children
            node.children[c] = next_node
            
        node = next_node

    # add an end of word trienode
    endNode = TrieNode(None, endOfWord=True)
    node.children[None] = endNode



	# return the number of partial matches to pat in the trie
	# return -1 if pat doesn't exist
	'''
	find the number of words that start with the string pat
	:type pat: string
    :rtype: int
    '''
	def find_partial(self, pat):
		node = self.root
		for c in pat:
			next_node = node.children.get(c, None)
			if next_node is None:
				return -1

			node = next_node
		else:

			# run a DFS on the tree to get the number of full words
			return self.explorer(node)
	'''
	recursive DFS to count the number of complete words
	:type node: TrieNode
    :rtype: int
    '''
    def explorer(self, node):
        # if the node's value is None, its an end of word node
        if node.val is None:
            return 1
        words = 0
        for node in node.children.values():
            words += self.explorer(node)
        return words






def main():
	tree = Trie()
	tree.insert("hello")
	print tree.find_partial("hello")


if __name__ == "__main__":
	main()