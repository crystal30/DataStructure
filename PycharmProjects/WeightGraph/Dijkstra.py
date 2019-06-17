from IndexMinHeap1 import IndexMinHeap
class Dijkstra:
    def __init__(self, graph,s):
        self.graph = graph
        self.imh = IndexMinHeap()
        self.marked = [False]*graph.V()
        self.distTo = [None]*graph.V()
        self.fromTo = [None]*graph.V()
        #对起始点s进行初始化
        self.distTo[s] = 0
        self.imh.add(s, self.distTo[s])
        while not self.imh.isEmpty():
            v = self.imh.extraMaxIndex()
            self.marked[v] = True
            it = self.graph.adj(v)
            # 遍历与v的邻边
            for E in it:
                w = E.other(v)
                # 如果从s点到w点的最短路径还没有找到
                if not self.marked[w]:
                    if self.distTo[w] == None or self.distTo[w] > self.distTo[v] + E.wt():
                        self.distTo[w] = self.distTo[v] + E.wt()
                        self.fromTo[w] = E
                        if not self.imh.contains(w):
                            self.imh.add(w, self.distTo[w])
                        else:
                            self.imh.change(w, self.distTo[w])

    #返回从s点到w点的最短路径长度
    def shortestPathWeightTo(self, w):
        assert self.hasPathTo(w), "s must be able to w"
        return self.distTo[w]

    # 判断从s点到w点是否联通
    def hasPathTo(self, w):
        assert w >= 0 and w <self.graph.V(), "w is invalid"
        return self.marked[w]

    #寻找从s到w的最短路径, 将整个路径经过的边存放在vec中
    def shortestPath(self, w):
        assert self.hasPathTo(w), "s must be able to w"
        mystack = []
        E = self.fromTo[w]
        while E is not None:
            mystack.append(E)
            v = E.other(w)
            E = self.fromTo[v]
            w = v
        mystack.reverse()
        return mystack

    #打印出从s点到w点的路径
    def showPath(self,w):
        path = self.shortestPath(w)
        for i in range(len(path)):
            print(str(path[i].v()) + '-->', end="")
            if i == len(path)-1:
                print(str(path[i].w()))








