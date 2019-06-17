class BellmanFord:
    def __init__(self, graph, s):
        self.graph = graph
        self.hasNegativeCycle = False
        self.fromTo = [None]*graph.V()
        self.distTo = [None]*graph.V()
        self.distTo[s] = 0

        #整体的时间复杂度 O(VE)
        #进行V-1次循环, 每一次循环求出从起点到其余所有点, 最多使用pass步可到达的最短距离,复杂度O(V)
        for p in range(1,graph.V()):

            # 每次循环中对所有的边进行一遍松弛操作
            # 遍历所有边的方式是先遍历所有的顶点, 然后遍历和所有顶点相邻的所有边,复杂度O（E）
            for v in range(graph.V()):
                it = graph.adj(v)
                # 对于每一个边首先判断E.v()可达
                # 之后看如果E.w(), 以前没有到达过， 显然我们可以更新distTo[E.w()]
                # 或者e->w()以前虽然到达过, 但是通过这个e我们可以获得一个更短的距离, 即可以进行一次松弛操作, 我们也可以更新distTo[e->w()]
                for E in it:
                    if self.distTo[v] != None and \
                            self.distTo[E.other(v)] == None or \
                            self.distTo[E.other(v)] > self.distTo[v] + E.wt():
                        self.distTo[E.other(v)] = self.distTo[v] + E.wt()
                        self.fromTo[E.other(v)] = E

        self.hasNegativeCycle = self.__detectNegativeCycle()

    def __detectNegativeCycle(self):
        #进行第V次松弛操作，若还能再松弛，说明图中有负权环
        for v in range(self.graph.V()):
            it = self.graph.adj(v)
            # 对于每一个边首先判断E.v()可达
            # 之后看如果E.w(), 以前没有到达过， 显然我们可以更新distTo[E.w()]
            # 或者e->w()以前虽然到达过, 但是通过这个e我们可以获得一个更短的距离, 即可以进行一次松弛操作, 我们也可以更新distTo[e->w()]
            for E in it:
                if self.distTo[v] != None and \
                        self.distTo[E.other(v)] == None or \
                        self.distTo[E.other(v)] > self.distTo[v] + E.wt():
                    self.distTo[E.other(v)] = self.distTo[v] + E.wt()
                    self.fromTo[E.other(v)] = E
                    return True
        return False

    # 返回图中是否有负权环
    def negativeCycle(self):
        return self.hasNegativeCycle

    # 返回从s点到w点的最短路径长度
    def shortestPathWeightTo(self, w):
        assert self.hasPathTo(w), "s must be able to w"
        assert not self.hasNegativeCycle, "There is a negative weight cycle in the graph"
        return self.distTo[w]

    #判断从s点到w点是否联通
    def hasPathTo(self, w):
        assert w >= 0 and w<self.graph.V(), "w is invalid"
        return self.fromTo[w] != None

    #寻找从s到w的最短路径, 将整个路径经过的边存放在vec中
    def shortestPath(self, w):
        assert self.hasPathTo(w), "s must be able to w"
        assert not self.hasNegativeCycle, "There is a negative weight cycle in the graph"
        mystack = []
        E = self.fromTo[w]
        while E is not None:
            v = E.other(w)
            mystack.append(E)
            E = self.fromTo[v]
            w = v
        mystack.reverse()
        return mystack

    # 打印出从s点到w点的路径
    def showPath(self, w):
        path = self.shortestPath(w)
        for i in range(len(path)):
            print(str(path[i].v()) + '-->', end="")
            if i == len(path)-1:
                print(str(path[i].w()))









