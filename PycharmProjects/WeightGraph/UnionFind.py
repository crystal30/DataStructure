# -*- coding: utf-8 -*-
# 路径压缩 path Compression,使用递归的方式实现

class UnionFind():
    def __init__(self,size):
        self.parent = [_ for _ in range(size)]
        self.nodeRank = [1]*size

    def __find(self,p):

        # 路径压缩2
        # 另一种形状
        #           0
        #          ／                    0
        #          1                 / / \ \
        #         ／   路径压缩       1  2 3 4
        #         2   -------->
        #        ／
        #        3
        #       ／
        #       4
        # 不过使用了递归可能会有一定的时间消耗
        # if p == self.parent[p]:
        #     return p # 等价于 return self.parent[p]

        if p != self.parent[p]:
            self.parent[p] = self.__find(self.parent[p])
        return self.parent[p]

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


