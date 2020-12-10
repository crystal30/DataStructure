class Solution:
    def uniquePaths(self, m: int, n: int):
        if m == 1 or n == 1:
            return 1

        memo = [[-1 for _ in range(n)] for _ in range(m)]

        for j in range(n - 1):
            memo[m - 1][j] = 1

        for i in range(m - 1):
            memo[i][n - 1] = 1

        memo[m - 1][n - 1] = 0

        for i in range(1, m):
            for j in range(1, n):
                memo[m - i - 1][n - j - 1] = memo[m - i - 1][n - j] + memo[m - i][n - j - 1]

        return memo[0][0]



class Solution2:
    def __init__(self):
        self.memo = None
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1 for _ in range(n)]  for _ in  range(m)]
        return self._unique_paths(m, n, 0, 0)

    def _unique_paths(self, m, n, x, y):
        if self.memo[x][y] != -1:
            return self.memo[x][y]

        if x == m-1 and y == n-1:
            self.memo[x][y] = 1
        elif x == m-1:
            self.memo[x][y] = self._unique_paths(m, n, x, y+1)
        elif y == n-1:
            self.memo[x][y] = self._unique_paths(m, n, x+1, y)
        else:
            self.memo[x][y] = self._unique_paths(m, n, x, y + 1) + self._unique_paths(m, n, x + 1, y)

        return self.memo[x][y]


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)]  for _ in  range(m)]
        for i in range(m):
            memo[i][n-1] = 1

        for i in range(n):
            memo[m-1][i] = 1

        row = [_ for _ in range(m - 1)]
        col = [_ for _ in range(n - 1)]

        for i in row[::-1]:
            for j in col[::-1]:
                memo[i][j] = memo[i+1][j] + memo[i][j+1]

        return memo[0][0]


if __name__ == "__main__":
    so = Solution3()
    re = so.uniquePaths(3, 2)
    print(re)






























