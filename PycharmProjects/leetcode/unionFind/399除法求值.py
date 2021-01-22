class UnionFind:
    def __init__(self, size):
        self.parent_id = [i for i in range(size)]
        self.weights = [1 for _ in range(size)]

    # 实现路径压缩,找到根结点的id
    def find(self, val):
        if val != self.parent_id[val]:
            ori_id = self.parent_id[val]
            self.parent_id[val] = self.find(self.parent_id[val])
            self.weights[val] = self.weights[val] * self.weights[ori_id]

        return self.parent_id[val]

    def union(self, val1, val2, weight):
        val1_parent_id = self.find(val1)
        val2_parent_id = self.find(val2)
        if val1_parent_id == val2_parent_id:
            return

        self.parent_id[val1_parent_id] = val2_parent_id
        self.weights[val1_parent_id] = self.weights[val2] * weight / self.weights[val1]
        return

    def isConnect(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return self.weights[x] / self.weights[y]
        return -1

class Solution:
    def calcEquation(self, equations, values, queries):
        val_map = dict()
        id = 0
        union_find = UnionFind(2 * len(equations))

        for i, (dividend, divisor) in enumerate(equations):
            if dividend not in val_map.keys():
                val_map[dividend] = id
                id += 1
            if divisor not in val_map.keys():
                val_map[divisor] = id
                id += 1
            union_find.union(val_map[dividend], val_map[divisor], values[i])

        re = [-1.0 for _ in range(len(queries))]
        for i, (dividend, divisor) in enumerate(queries):
            if dividend not in val_map.keys() or divisor not in val_map.keys():
                continue
            re[i] = union_find.isConnect(val_map[dividend], val_map[divisor])

        return re

if __name__ == '__main__':
    so = Solution()
    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    re = so.calcEquation(equations, values, queries)
    print(re)










