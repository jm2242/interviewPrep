class TrieNode(object):
    def __init__(self,val,endOfWord=False):
        self.children = {}
        self.val = val
        self.endOfWord = endOfWord
    def __str__(self):
        return "value: {0} children: {1}".format(self.val,self.children)
class Trie(object):

    def __init__(self, val=None, endOfWord=True):
        self.root = TrieNode(val, endOfWord)
        self.levels = 0

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
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

        

    def search(self, pat):
        """
        Returns if the word pat is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in pat:
            next_node = node.children.get(c, None)
            if next_node is None:
                return False

            node = next_node
        else:
            return (None in node.children)


        

    def startsWith(self, pat):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in pat:
            next_node = node.children.get(c, None)
            if next_node is None:
                return False

            node = next_node
        else:
            return (len(next_node.children) > 0)
        


if __name__ == "__main__":
    trie = Trie()
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")