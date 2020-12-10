class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                    continue

                if j == 0:
                    grid[i][j] += grid[i-1][j]
                    continue

                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]


class Solution2:
    def __init__(self):
        self.memo = None
        self.m = 0
        self.n = 0

    def minPathSum(self, grid):
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])

        self.memo = [[-1 for _ in range(self.m)] for _ in range(self.n)]
        return self._min_path_sum(grid, 0, 0)

    def _min_path_sum(self, grid, x, y):

        if self.memo[x][y] != -1:
            return self.memo[x][y]

        if x+1 < self.m:
            re_down = self._min_path_sum(grid, x+1, y)
        else:
            re_down = -1

        if y+1 < self.n:
            re_right = self._min_path_sum(grid, x, y+1)
        else:
            re_right = -1

        if re_down == -1 and re_right == -1:
            self.memo[x][y] = grid[x][y]
        elif re_down == -1:
            self.memo[x][y] = grid[x][y] + re_right
        elif re_right == -1:
            self.memo[x][y] = grid[x][y] + re_down
        else:
            self.memo[x][y] = grid[x][y] + min(re_right, re_down)

        return self.memo[x][y]


class Solution3:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        row_num = [i for i in range(m)]
        col_num = [j for j in range(n)]
        for i in row_num[::-1]:
            for j in col_num[::-1]:
                if i+1 >= m and j+1 >= n:
                    continue
                elif i+1 >= m:
                    grid[i][j] += grid[i][j+1]

                elif j+1 >= n:
                    grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] += min(grid[i][j+1], grid[i+1][j])

        return grid[0][0]


if __name__ == "__main__":
    so = Solution3()
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    re = so.minPathSum(grid)
    print(re)





















