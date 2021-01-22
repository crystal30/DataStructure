class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y
        return


class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        union_find = UnionFind(n)
        re = None
        for u, v in edges:
            if union_find.find(u) == union_find.find(v):
                re = [u, v]
                continue
            union_find.union(u, v)

        return re


if __name__ == '__main__':
    so = Solution()
    edages = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    re = so.findRedundantConnection(edages)
    print(re)






