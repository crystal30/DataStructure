# -*- coding: utf-8 -*-
#并差集优化，基于rank
class UnionFind():
    def __init__(self,size):
        self.parent = [_ for _ in range(size)]
        self.nodeRank = [1]*size #self.nodeRank[i] 表示跟节点为i的树的高度

    # 返回元素p所在的根节点
    def __find(self,p):
        assert p>=0 and p<len(self.parent), "p must be between 0 and size"
        while(p != self.parent[p]):
            p = self.parent[p]
        return p

    def isConnected(self,p,q):

        return self.__find(p) == self.__find(q)

    def union(self,p,q):
        prootId = self.__find(p)
        qrootId = self.__find(q)

        if self.nodeRank[prootId] > self.nodeRank[qrootId]:
            self.parent[qrootId] = prootId
        elif self.nodeRank[prootId] < self.nodeRank[qrootId]:
            self.parent[prootId] = qrootId
        else:# self.nodeRank[prootId] == self.nodeRank[qrootId]:
            self.parent[prootId] = qrootId # 也可以 self.parent[qrootId] = prootId
            self.nodeRank[qrootId] += 1


