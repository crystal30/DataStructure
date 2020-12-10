# coding:utf-8
class Solution:
    def __init__(self):
        self.memo = None

    def integerBreak(self, n: int):
        self.memo = [-1] * (n+1)
        self.memo[1] = 1
        self.memo[2] = 1 # 其至少分解成至少两个正整数的和
        for i in range(3, n+1):
            for j in range(1, i):
                self.memo[i] = max(self.memo[i], j * (i-j), j*self.memo[i-j])

        return self.memo[n]

class Solution1:
    def __init__(self):
        self.memo = None

    def integerBreak(self, n: int):
        self.memo = [-1] * (n+1)
        return self._max_integer_break(n)

    def _max_integer_break(self, n):
        if n == 1:
            return 1
        if self.memo[n] != -1:
            return self.memo[n]

        res = -1
        for i in range(1, n):
            res = max(res, i*(n-i), i*self._max_integer_break(n-i))

        self.memo[n] = res
        return res

class Solution3:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        memo = [0 for _ in range(n+1)]
        memo[1] = 1
        memo[2] = 2
        for i in range(3, n+1):
            max_memo_i = 0
            for j in range(1, i):
                memo_i = j * memo[i - j]
                if max_memo_i < memo_i:
                    max_memo_i = memo_i
            if i == n:
                memo[i] = max_memo_i
            else:
                memo[i] = max(i, max_memo_i)
        return memo[n]

if __name__ == "__main__":
    so = Solution3()
    re = so.integerBreak(10)
    print(re)





























