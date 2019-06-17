# -*- coding: utf-8 -*-
import numpy as np
class DenseGraph:
    def __init__(self, n, directed):
        self.n = n #节点数
        self.m = 0 #边数
        self.directed = directed
        #默认的，初始时邻接矩阵均为0，即没有一条边，用numpy
        # self.g = np.zeros(shape=(n, n), dtype= int)
        #不用numpy生成二维数组，初始时邻接矩阵全部时False
        self.g = [[0] * n for i in range(n)]

    #返回节点的个数
    def V(self):
        return self.n

    #返回边的条数
    def E(self):
        return self.m

    #添加边,v,w均是从0开始标记的
    def addEadge(self, v, w):
        #如果v，w之间已经有边了，则什么也不作，很好的处理了平行边的问题
        if self.hasEadge(v,w):
            return

        #在v，w两点之间不存在边的时候
        self.g[v][w] = 1

        #判断其是否时有向图，当不是有向图时，self.g[v][w]为1时，self.g[w][v] 也为1
        # 条件中加入了 v ！= w，很好的处理了自环边(即不会重复的添加自环边)
        if v != w and self.directed != True:
            self.g[w][v] = 1
        self.m += 1

    #判断点v和点w之间是否有边相连
    def hasEadge(self, v, w):
        assert v >= 0 and v < self.n, "v is invalid"
        assert w >= 0 and w < self.n, "w is invalid"
        return self.g[v][w]

    #返回图中一个顶点v的所有邻边
    # 输出的顶点v的所有邻边 均是从小到大排列的
    #如果遍历所有的顶点的所有的邻边，时间复杂度为O（n2）,n表示节点数
    def adj(self,v):
        re = []
        for i in range(self.V()):
            if self.g[v][i] == 1:
                re.append(i)
        return re

    def show(self):
        for i in range(self.V()):
            print(self.g[i])










