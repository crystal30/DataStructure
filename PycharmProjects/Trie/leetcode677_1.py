# -*- coding: utf-8 -*-
class Node():
    def __init__(self,val=0):
        self.next = dict()
        self.val = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = Node()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self.__root
        for c in key:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]
        cur.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.__root
        for pc in prefix:
            if pc not in cur.next:
                return 0
            cur = cur.next[pc]
        return self.__sum(cur)

    def __sum(self,node):

        sum = node.val
        #递归结束的条件
        if len(node.next) == 0:
            return sum
        #递归
        for c in node.next:
            sum += self.__sum(node.next[c])
        return sum

if __name__ == '__main__':
    sum = MapSum()
    sum.insert('aa',3)
    print(sum.sum('a'))
    sum.insert('ab', 2)
    print(sum.sum('a'))