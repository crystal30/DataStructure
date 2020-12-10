# -*- coding:utf-8 -*-
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])

        memo = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        else:
            memo[m-1][n-1] = 1

        for i in range(1, m):
            if obstacleGrid[m-i-1][n-1] != 1:
                memo[m-i-1][n-1] += memo[m-i][n-1]

        for j in range(1, n):
            if obstacleGrid[m-1][n-j-1] != 1:
                memo[m-1][n-j-1] += memo[m-1][n-j]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[m - i - 1][n - j -1] != 1:
                    memo[m - i - 1][n - j -1] = \
                        memo[m - i - 1][n - j] + memo[m - i][n - j -1]


        return memo[0][0]

class Solution3:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.memo = None
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        if self.n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        self.memo = [[-1 for _ in range(self.n)] for _ in range(self.m)]
        return self._unique_path(0, 0, obstacleGrid)

    def _unique_path(self, x, y, obstacleGrid):
        if self.memo[x][y] != -1:
            return self.memo[x][y]

        if x == self.m - 1 and y == self.n - 1:
            if obstacleGrid[x][y] != 1:
                self.memo[x][y] = 1
            else:
                self.memo[x][y] = 0

        elif x == self.m - 1: # 只能向右走
            if obstacleGrid[x][y+1] != 1:
                self.memo[x][y] = self._unique_path(x, y+1, obstacleGrid)
            else:
                self.memo[x][y] = 0

        elif y == self.n - 1: # 只能向下走
            if obstacleGrid[x+1][y] != 1:
                self.memo[x][y] = self._unique_path(x+1, y, obstacleGrid)
            else:
                self.memo[x][y] = 0
        else:
            if obstacleGrid[x+1][y] == 1 and obstacleGrid[x][y+1] == 1:
                self.memo[x][y] = 0
            elif obstacleGrid[x+1][y] == 1:
                self.memo[x][y] = self._unique_path(x, y + 1, obstacleGrid)
            elif obstacleGrid[x][y+1] == 1:
                self.memo[x][y] = self._unique_path(x + 1, y, obstacleGrid)
            else:
                self.memo[x][y] = self._unique_path(x, y+1, obstacleGrid) + self._unique_path(x+1, y, obstacleGrid)


        return self.memo[x][y]


class Solution4:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if n == 0:
            return 1

        if obstacleGrid[0][0] == 1:
            return 0

        if obstacleGrid[m - 1][n - 1] == 1:
            return 0

        memo = [[-1 for _ in range(n)] for _ in range(m)]
        memo[m-1][n-1] = 1
        row_num = [_ for _ in range(m-1)]
        col_num = [_ for _ in range(n-1)]
        # 最后一列，只能向下
        for i in row_num[::-1]:
            if obstacleGrid[i][n-1] != 1:
                memo[i][n-1] = memo[i+1][n-1]
            else:
                memo[i][n-1] = 0

        # 最后一行，只能向右
        for j in col_num[::-1]:
            if obstacleGrid[m-1][j] != 1:
                memo[m-1][j] = memo[m-1][j+1]
            else:
                memo[m - 1][j] = 0

        for i in row_num[::-1]:
            for j in col_num[::-1]:
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i+1][j] + memo[i][j+1]

        return memo[0][0]



if __name__ == "__main__":
    so = Solution4()
    obstacleGrid = [[0]]
    re = so.uniquePathsWithObstacles(obstacleGrid)
    print(re)