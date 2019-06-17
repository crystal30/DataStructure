# -*- coding: utf-8 -*-
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph
from UnicomComponent import UnicomComponent
#从文件filename中读取图的信息, 存储进图graph中
class ReadGraph:
    def __init__(self, filename, graph):
        fo = open(filename, "r")
        n, m = map(int, fo.readline().split(' '))
        self.graph = graph(n,False)
        for line in fo.readlines():
            v, w = map(int, line.split(' '))
            self.graph.addEadge(v, w)

    def V(self):
        return self.graph.V()

    def E(self):
        return self.graph.E()

    def adj(self,v):
        return self.graph.adj(v)
    def show(self):
        return self.graph.show()







