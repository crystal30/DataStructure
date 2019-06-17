#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node:
    def __init__(self):
        self.next = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.__root = Node()
        self.__size = 0

    #获得Trie中存储的单词数量
    def getSize(self):
        return self.__size

    #向Trie中添加一个新的字符串 string
    def add(self,string):
        cur = self.__root
        for c in string:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]

        if not cur.isWord:
            cur.isWord = True
            self.__size += 1

    #查询字符串string是否在Trie中
    def contains(self,string):
        cur = self.__root
        for c in string:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return cur.isWord

    #查询是否在Trie中有字符串以prefix为前缀
    def isPerfix(self, prefix):
        cur = self.__root
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        return True

if __name__== '__main__':
    trie = Trie()
    for word in ['one','two','three']:
        trie.add(word)
    print(trie.contains('thr'))
    print(trie.contains('one'))
    print(trie.contains('two'))
    print(trie.contains('three'))







