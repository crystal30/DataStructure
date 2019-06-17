# -*- coding: utf-8 -*-
import random
from Edge import Edge
#稀疏图用邻接表来表示
class SparseGraph:
    def __init__(self, n, directed):
        self.n = n  #节点数 n>0
        self.m = 0  #边数 初始为0
        self.directed = directed  #是否为方向图
        #构造邻接表
        self.g = [None]*n
        for i in range(n):
            self.g[i] = []

    def V(self):
        return self.n

    def E(self):
        return self.m

    #添加边
    def addEadge(self, v, w, weight):
        #一般情况下可不判断v，w之间是否有边相连，因为加上这个判断，时间复杂度将变为O（n）
        if self.hasEadge(v, w):
            return

        #当v，w之间未相连时
        self.g[v].append(Edge(v,w,weight))
        #当不是有向图时
        #条件中加入了 v ！= w，很好的处理了自环边(即不会重复的添加自环边)
        if v != w and self.directed != True:
            self.g[w].append(Edge(w,v,weight))
        self.m += 1

    #查看v，w之间是否存在边,O(n)的复杂度，因为要遍历一遍self.g[v]这个向量的所有元素
    def hasEadge(self, v, w):
        assert v >= 0 and v < self.n, "v is invalid"
        assert w >= 0 and w < self.n, "w is invalid"
        for E in self.g[v]:
            if w == E.w():
                return True
        return False

    # 返回图中一个顶点v的所有邻边
    # 输出的顶点v的所有邻边 没有从小到大或从大到小排列，是根据其添加到邻接表的顺序排列的
    # 如果遍历所有的节点的所有邻边，时间复杂度为O(2m)
    def adj(self,v):
        return self.g[v]

    def show(self):
        for i in range(self.V()):
            re = str(i) + ': {'
            it = self.g[i]
            for j in range(len(it)):
                if j == len(it) - 1:
                    re += str(it[j].other(i)) + ':'+str(it[j].wt())
                else:
                    re += str(it[j].other(i)) + ':' + str(it[j].wt()) + ',\t'
            re += '}'
            print(re)

if __name__ == "__main__":

    sg = SparseGraph(10,False)
    v = random.randint(0, sg.V())
    w = random.randint(0, sg.V())


