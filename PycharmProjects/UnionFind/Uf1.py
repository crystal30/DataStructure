# -*- coding: utf-8 -*-
# 基于quickFind 实现并差集
class UnionFind:
    def __init__(self,size):
        #初始化, 每一个id[i],指向自己, 没有合并的元素
        self.id = [_ for _ in range(size)]


    def getSize(self):
        return len(self.id)

    # 查找元素p所对应的集合编号,O(1)复杂度
    def __find(self,p):
        assert p>=0 and p<len(self.id), "p must be between 0 and size"

        return self.id[p]

    # 查看元素p和元素q是否所属一个集合,O(1)复杂度
    def isConnected(self,p,q):
        return self.__find(p) == self.__find(q)

    #合并元素p和元素q所属的集合,O(n)复杂度
    def Union(self,p,q):
        #元素p所属的集合的ID
        psetID = self.__find(p)
        qsetID = self.__find(q)
        if  psetID == qsetID:
            return
        for i in range(len(self.id)):
            if self.id[i] == psetID:
                self.id[i] = qsetID

