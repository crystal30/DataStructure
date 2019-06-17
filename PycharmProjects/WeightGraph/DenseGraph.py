# -*- coding: utf-8 -*-
import numpy as np
from Edge import Edge
from copy import copy
class DenseGraph:
    def __init__(self, n, directed):
        self.n = n #节点数
        self.m = 0 #边数
        self.directed = directed
        #默认的，初始时邻接矩阵均为0，即没有一条边，用numpy
        # self.g = np.zeros(shape=(n, n), dtype= int)
        #不用numpy生成二维数组，初始时邻接矩阵全部时False
        self.g = [[None] * n for i in range(n)]

    #返回节点的个数
    def V(self):
        return self.n

    #返回边的条数
    def E(self):
        return self.m

    #添加边,v,w均是从0开始标记的
    def addEadge(self, v, w,weight):
        # 如果v，w之间已经有边了,什么也不做，很好的处理了平行边
        if self.hasEdge(v, w):
            return
        #如果v，w之间没有边
        self.g[v][w] = Edge(v, w, weight)

        #判断其是否时有向图，当不是有向图时，self.g[v][w]，self.g[w][v] 之间的边是一样的
        # 条件中加入了 v ！= w，很好的处理了自环边(即不会重复的添加自环边)
        if v != w and self.directed != True:
            self.g[w][v] = Edge(v, w, weight)
        self.m += 1

    #判断点v和点w之间是否有边相连
    def hasEdge(self, v, w):
        assert v >= 0 and v < self.n, "v is invalid"
        assert w >= 0 and w < self.n, "w is invalid"
        return False if self.g[v][w] == None else True

    #返回图中一个顶点v的所有邻边,及权重
    # 输出的顶点v的所有邻边 均是从小到大排列的
    #如果遍历所有的顶点的所有的邻边，时间复杂度为O（n2）,n表示节点数
    def adj(self,v):
        return self.g[v]

    def show(self):
        for i in range(self.V()):
            re = []
            for j in range(self.V()):
                if self.g[i][j] == None:
                    re.append(None)
                else:
                    re.append(self.g[i][j].wt())
            print(re)










