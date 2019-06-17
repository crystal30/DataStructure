#图的广度优先遍历（Breadth-first search） ，求s到某个点的最短路径
class ShortPath:
    def __init__(self,graph,s):
        self.graph = graph
        self.visited = [False]*graph.V()
        self.pathfrom = [-1]*graph.V()
        self.order = [-1]*graph.V() #记录路径中节点的次序。ord[i]表示i节点在路径中的次序。
        self.queue = []
        self.visited[s] = True
        self.order[s] = 0
        self.bfs(s)

    def bfs(self,v):
        it = self.graph.adj(v)
        for i in it:
            if not self.visited[i]:
                self.queue.append(i)
                self.visited[i] = True
                self.pathfrom[i] = v
                self.order[i] = self.order[v]+1
        while len(self.queue) != 0:
            self.bfs(self.queue.pop(0))

    def path(self,w):
        assert self.hasPath(w), "s can not go to w"
        stack = []
        p = w
        while p != -1:
            stack.append(p)
            p = self.pathfrom[p]
        stack.reverse()
        return stack



    def hasPath(self, w):
        return self.visited[w]

    def showPath(self,w):
        spath = self.path(w)
        str_spath = [str(_) for _ in spath]
        print('-->'.join(str_spath))

    # （针对无权图)查看从s点到w点的最短路径长度
    # 若从s到w不可达，返回 - 1
    def length(self,w):
        if self.hasPath(w):
            return self.order[w]
        return -1









