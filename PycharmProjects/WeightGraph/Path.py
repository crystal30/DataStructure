#用图的深度优先遍历（Depth-first search），寻找图graph从s点到其他点的路径
class Path():
    def __init__(self, graph, s):
        self.graph = graph
        self.pathfrom = [-1]*graph.V()
        self.visited = [False]*graph.V()
        self.dfs(s)


    def dfs(self, v):
        self.visited[v] = True
        it = self.graph.adj(v)
        for i in it:
            if not self.visited[i]:
                self.pathfrom[i] = v #表示访问时，i这个节点的前一个节点时v
                self.dfs(i)

    #查询从s点到w点是否有路径
    def hasPath(self, w):
        return self.visited[w]

    #查询从s点到w点的路径
    def path(self, w):
        stack = []
        p = w
        while p != -1:
            stack.append(p)
            p = self.pathfrom[p]
        stack.reverse()
        return stack
    def showPath(self,w):
        st = self.path(w)
        str_st = [str(_) for _ in st]
        print('-->'.join(str_st))





