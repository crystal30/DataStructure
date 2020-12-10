class Solution:
    def __init__(self):
        self.memo = None
    def numSquares(self, n: int):
        self.memo = [float("inf")] * (n+1)
        self.memo[0] = 0
        self.memo[1] = 1

        for i in range(2, n+1):
            square_max = int(i ** (1 / 2))
            for j in range(1, square_max+1):
                self.memo[i] = min(self.memo[i], 1 + self.memo[i - j*j])

        return self.memo[n]

class Solution1:
    def __init__(self):
        self.memo = None
    def numSquares(self, n: int):
        self.memo = [-1] * (n+1)
        self.memo[0] = 0
        self.memo[1] = 1
        return self._num_square(n)

    def _num_square(self, n):
        if self.memo[n] != -1:
            return self.memo[n]

        res = 1000000000

        square_max = n ** (1/2)
        int_square_max = int(square_max)
        for j in range(1, int_square_max+1):
            res = min(res, 1 + self._num_square(n - j*j))

        self.memo[n] = res
        return res

class Solution2:
    def numSquares(self, n: int) -> int:
        if n <= 3:
            return n
        if n % (n**0.5) == 0:
            return 1
        memo = [0]*(n+1)
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3

        for i in range(4, n+1):
            if memo[i] != 0:
                continue
            min_i_memo = i
            for j in range(1, int(i**0.5)+1):
                min_i_memo = min(min_i_memo, memo[i-j**2]+1)
            memo[i] = min_i_memo

        return memo[n]

if __name__ == "__main__":
    so = Solution2()
    re = so.numSquares(5)
    print(re)

























