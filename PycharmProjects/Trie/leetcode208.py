class Node():
    def __init__(self):
        self.next = dict()
        self.isword = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.__root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]
        if not cur.isword:
            cur.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.__root
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return cur.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.__root
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)