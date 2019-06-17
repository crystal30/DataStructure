# -*- coding: utf-8 -*-
# 路径压缩 path Compression

class UnionFind():
    def __init__(self,size):
        self.parent = [_ for _ in range(size)]
        self.nodeRank = [1]*size

    def __find(self,p):
        # 路径压缩1
        # 实现的形状
        #           0
        #          ／                 0
        #          1                 / \
        #         ／   路径压缩       1  2
        #         2   -------->        /\
        #        ／                    3 4
        #        3
        #       ／
        #       4
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
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
        else:
            self.parent[prootId] = qrootId
            self.nodeRank[qrootId] += 1


