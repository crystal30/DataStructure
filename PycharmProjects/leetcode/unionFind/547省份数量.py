class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return
        self.parent[rootx] = rooty
        return

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)

        root_set = set()
        for i in range(n):
            root_set.add(union_find.find(i))

        return len(root_set)

if __name__ == '__main__':
    so = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    re = so.findCircleNum(isConnected)
    print(re)

