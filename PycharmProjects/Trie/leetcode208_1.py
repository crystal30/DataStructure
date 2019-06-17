#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用递归的方式
class Node():
    def __init__(self):
        self.next = dict()
        self.isWord = False

class Trie():
    def __init__(self):
        self.__root = Node()

    def insert(self, word):
        self.__add(self.__root, word)

    def __add(self, node, string):
        # 递归结束的条件
        if len(string) == 1:
            if string not in node.next:
                node.next[string] = Node()
            node.next[string].isWord = True
            return
        # 递归
        if len(string) >1:
            if string[0] not in node.next:
                node.next[string[0]] = Node()
            self.__add(node.next[string[0]], string[1:])

    def search(self, word):
        return self.__contains(self.__root, word)

    def __contains(self, node, string):
        #递归结束的条件
        if len(string) == 1:
            if string in node.next:
                return node.next[string].isWord
            else:
                return False
        if len(node.next) == 0 :
            return False

        #递归
        if len(node.next) > 0 and len(string)>1:
            if string[0] in node.next:
                return self.__contains(node.next[string[0]], string[1:])
            else:
                return False

    def startsWith(self, prefix):
        return self.__prefix(self.__root, prefix)

    def __prefix(self, node, pre):

        #两个递归结束的条件
        if len(pre) == 1:
            if pre[0] in node.next:
                return True
            else:
                return False
        if len(node.next) == 0:
            return False
        #递归
        if len(node.next) > 0 and len(pre)>1:
            if pre[0] in node.next:
                return self.__prefix(node.next[pre[0]], pre[1:])
            else:
                return False