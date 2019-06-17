# -*- coding: utf-8 -*-
# 并差集优化 ，基于size
class UnionFind():
    def __init__(self, size):
        # 初始化parent，每个节点都指向自己，是一颗独立的树（即此时两两节点互不相连）
        self.parent = [_ for _ in range(size)]
        self.nodeSize = [1]*len(size)

    def __find(self, p):
        assert p >= 0 and p < len(self.parent), "p must be between 0 and size"
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        prootId = self.__find(p)
        qrootId = self.__find(q)
        if prootId == qrootId:
            return
        # 由于 prootId 是跟节点，所以自己指向自己，下标和元素相同，parent[prootId]=prootId
        if self.nodeSize[qrootId] > self.nodeSize[prootId]:
            self.parent[prootId] = qrootId
            self.nodeSize[qrootId] += self.nodeSize[prootId]
        else:
            self.parent[qrootId] = prootId
            self.nodeSize[prootId] += self.nodeSize[qrootId]

    def isConnected(self, p, q):
        prootId = self.__find(p)
        qrootId = self.__find(q)
        return prootId == qrootId


