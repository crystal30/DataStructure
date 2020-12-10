# 用递归的思想，解决0-1背包问题
class Solution:
    def __init__(self):
        self.w = None
        self.v = None
        self.memo = None

    def knapsack(self, w, v, c):
        """
        将重量为w,价值为v的n个物品，放进容量为c的背包中，使得价值最大
        :param w: list 为物体的重量，长度为n
        :param v: list 为物体的价值，长度为n
        :param c: const，为物体的容量
        :return:
        """
        n = len(w)
        self.w = w
        self.v = v
        self.memo = [[-1 for _ in range(c+1)] for _ in range(n)]
        return self.value_knapsack(n-1, c)

    def value_knapsack(self, index, c):
        """
        用[0, index]的物品，填充容量为c的背包所能有的最大的价值
        :param index:
        :param c:
        :return:
        """
        if c <= 0 or index < 0:
            return 0

        if self.memo[index][c] != -1:
            return self.memo[index][c]

        res = self.value_knapsack(index-1, c)
        w_index = self.w(index)
        if w_index <= c:
            res = max(res, self.v(index) + self.value_knapsack(index-1, c-w_index))

        self.memo[index][c] = res
        return res


# 用动态规划的思想，解决0-1背包问题
class Solution1:

    def knapsack(self, w, v, c):
        """
        将重量为w,价值为v的n个物品，放进容量为c的背包中，使得价值最大
        :param w: list 为物体的重量，长度为n
        :param v: list 为物体的价值，长度为n
        :param c: const，为物体的容量
        :return:
        """
        n = len(w)
        if n == 0:
            return 0
        memo = [[0 for _ in range(c+1)] for _ in range(n)]
        for j in range(c+1):
            if j >= w[0]:
                memo[0][j] = v[0]

        for i in range(1, n):
            for j in range(c+1):
                res = memo[i-1][j]
                if w(i) <= j:
                    res = max(res, v[i] + memo[i-1][j-w(i)])
                memo[i][j] = res

        return memo[n-1][c]


# 用动态规划的思想，解决0-1背包问题
# 继续优化空间复杂度
class Solution2:
    def knapsack(self, w, v, c):
        """
        将重量为w,价值为v的n个物品，放进容量为c的背包中，使得价值最大
        :param w: list 为物体的重量，长度为n
        :param v: list 为物体的价值，长度为n
        :param c: const，为物体的容量
        :return:
        """
        n = len(w)
        if n == 0 or c == 0:
            return 0
        memo = [0 for _ in range(c+1)]
        for j in range(c+1):
            if j >= w[0]:
                memo[j] = v[0]

        for i in range(1, n):
            for j in range(c, -1, -1):
                res = memo[j]
                if w(i) <= j:
                    res = max(res, v[i] + memo[j-w(i)])
                memo[j] = res

        return memo[c]




