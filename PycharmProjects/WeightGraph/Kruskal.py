from MInHeap import MinHeap
from UnionFind import UnionFind
class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        self.mst = []
        self.minh = MinHeap()
        self.Uf = UnionFind(graph.V())
        #将所有的边推入到最小堆中，由于是无向图，剔除掉重复的边,复杂度O(Elog(E))
        for i in range(graph.V()):
            it = graph.adj(i) #由于是无向图，所以会有重复的边，用E.v() < E.w()来剔除另一半重复的边
            for E in it:
                if E.v() < E.w():
                    self.minh.add(E)
        #当最小堆为空，或是所有的点都已经遍历完时，结束
        #所有的边取出来且判断一下其是否形成环，复杂度，O(Elog(V))
        while not self.minh.isEmpty() and len(self.mst) < self.graph.V():
            minE = self.minh.extractMin()
            if not self.Uf.isConnected(minE.v(), minE.w()):
                self.mst.append(minE)
                self.Uf.union(minE.v(), minE.w())

    def mstEdges(self):
        return self.mst

    def mstWeight(self):
        mstw = []
        for E in self.mst:
            mstw.append(E.wt())
        return mstw

    # 返回最小生成树的权值
    def minWeight(self):
        mstw = self.mstWeight()
        return sum(mstw)



