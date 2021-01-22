# -*- coding: utf-8 -*-
# 该方法超时
class Solution:
    def numTrees(self, n: int):
        # 看一下等于0的情况是否符合
        if n <= 1:
            return 1
        if n == 2:
            return 2

        re = 0
        for i in range(1, n+1):
            re += self.numTrees(i - 1) * self.numTrees(n - i)
        return re


# 用记忆化搜索的方式
class Solution1:
    def __init__(self):
        self.memo = None

    def numTrees(self, n: int):
        self.memo = [-1 for _ in range(n+1)]
        return self._num_trees(n)

    def _num_trees(self, n):
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if self.memo[n] != -1:
            return self.memo[n]

        re = 0
        for i in range(1, n+1):
            re += self._num_trees(i - 1) * self._num_trees(n - i)

        self.memo[n] = re
        return re


if __name__ == '__main__':
    so = Solution1()
    n = 3
    re = so.numTrees(n)
    print(re)
