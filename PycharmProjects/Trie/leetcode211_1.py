# -*- coding: utf-8 -*-
class Node():
    def __init__(self):
        self.next = dict()
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.__root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]

        if not cur.isWord:
            cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__search(self.__root, word,0)

    def __search(self, node, word,index):

        if index==len(word):
            return node.isWord

        c = word[index]
        if c is not '.':
            if c not in node.next:
                return False
            else:
                return self.__search(node.next[c],word,index+1)
        else: # c is '.'
            # 与leetcode211.py 略有不同，代码更简洁一点
            for nextchar in node.next.keys():
                if self.__search(node.next[nextchar],word,index+1):
                    return True
            return False
# ["WordDictionary","addWord","addWord","addWord","addWord",  "search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],    ["a"],[".at"],  ["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

if __name__ == '__main__':
    wo = WordDictionary()
    wo.addWord('at')
    wo.addWord('and')
    wo.addWord('an')
    wo.addWord('add')
    print(wo.search('a'))
    print(wo.search('.at'))

    wo.addWord('bat')
    print(wo.search('.at'))
