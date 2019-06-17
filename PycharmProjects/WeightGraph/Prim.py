from IndexMinHeap import IndexMinHeap
#求最小生成树，v个节点，v-1条边，且边的权值相加最小
#与LazyPrim 相比，改进的地方
#1。最小索引堆中不包含不是横切边的边
#2。最小索引堆中只包含最短的横切边（通过不断的更新和每个节点的最小的横切边得到）
#3.除了对堆的改进，遍历的次数也变少了
#n表示节点的个数， m表示边的条数
#该算法的时间复杂度 Omlogm
from IndexMinHeap import IndexMinHeap
class PrimMST():
    def __init__(self, graph):
        self.graph = graph
        self.edge = [None]*self.graph.V()
        self.imh = IndexMinHeap(self.graph.V())
        self.mst = []    #存储最小路径的边
        self.marked = [False] * self.graph.V() #初始时，所有的节点都标记为False
        self.visit(0) #从节点0开始 构造最小生成树

        #由于我们初始化时让最小堆中self.data = [float('inf')]*capacity，此处capacity为graph.V()，
        # 节点的个数，所以最小堆中，最终，self.indexs= [0], self.data[0] = inf
        while self.imh.getSize() > 1:
            index = self.imh.extraMin() #返回最小的横切边的另一个节点
            self.mst.append(self.edge[index])
            self.visit(index)
    #访问某个节点i，将节点i符合条件（最小的横切边）的邻边插入到最小堆中，初始时，最小堆中的元素均为inf
    def visit(self, i):
        self.marked[i] = True
        it = self.graph.adj(i)
        for E in it:
            #判断是否是横切边，且是否是最小的横切边
            if not self.marked[E.other(i)]:
                if self.edge[E.other(i)] == None or self.edge[E.other(i)] > E:
                    self.edge[E.other(i)] = E
                    self.imh.change(E.other(i),E.wt())

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

