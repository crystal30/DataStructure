#计算联通分量
#注意：联通分量和联通分量之间没有任何边相连
class UnicomComponent:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False]*graph.V()
        self.id = [None]*graph.V()
        self.ccount = 0
        for v in range(graph.V()):
            if not self.visited[v]:
                self.dfs(v)
                self.ccount += 1

    #以v 为节点进行深度优先遍历，即遍历一遍与v相连(不单单时邻边)的所有节点
    def dfs(self, v):
        self.visited[v] = True
        self.id[v] = self.ccount
        it = self.graph.adj(v)
        for i in it:
            if not self.visited[i]:
                self.dfs(i)

    def count(self):
        return self.ccount

    #判断点p和点q是否相连接，
    def isConnected(self,v,w):
        return self.id[v] == self.id[w]









