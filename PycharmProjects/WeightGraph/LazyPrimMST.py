from MInHeap import MinHeap
#求最小生成树，v个节点，v-1条边，且边的权值相加最小
#n表示节点的个数， m表示边的条数
#该算法的时间复杂度 Omlogm
class LazyPrimMST():
    def __init__(self, graph):
        self.marked = [False] * graph.V()
        self.graph = graph
        self.mh = MinHeap()  # 最小堆
        self.mst = []
        self.__visit(0)
        #所有的边都会进入mh，所以，下边的循环会执行m次（边的个数）
        while self.mh.getSize() != 0:
            E = self.mh.extractMin()  # 推出权重最小的邻边  复杂度O(logm),因为其中最多元素可能有m个
            if self.marked[E.v()] != self.marked[E.w()]:  # 当边两边的节点不属于同一个切片时即为横切边
                self.mst.append(E.wt())
                if not self.marked[E.v()]:
                    self.__visit(E.v())
                elif not self.marked[E.w()]:
                    self.__visit(E.w())
    def __visit(self, v):
        it = self.graph.adj(v)  # 从节点0开始搜寻最小生成树，it存储的为0的邻边
        for items in it:
            if items != None:
                self.mh.add(items)  # 将节点0的邻边存入到 最小堆中 复杂度O(m),在邻接矩阵中，稠密图n2约等于m

    #返回最小生成树的所有边
    def mstEdges(self):
        return self.mst

    # 返回最小生成树的权值
    def minWeight(self):
        return sum(self.mst)
