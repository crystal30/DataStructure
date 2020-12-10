# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.grid_rows = None
        self.grid_columns = None
        # 上 下 左 右 四个方向
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.startx = None
        self.starty = None
        self.visited = None

    def numIslands(self, grid):
        self.grid_rows = len(grid)
        if self.grid_rows == 0:
            return 0
        self.grid_columns = len(grid[0])
        self.visited = [[False for i in range(self.grid_columns)] for j in range(self.grid_rows)]
        res = 0
        for i in range(self.grid_rows):
            for j in range(self.grid_columns):
                if not self.visited[i][j]:
                    self.startx = i
                    self.starty = j
                    if self._num_is_lands(grid, i, j) == True:
                        res += 1
        return res


    def _num_is_lands(self, grid, startx, starty):
        if grid[startx][starty] == '0':
            return False

        if self.visited[startx][starty] == True and \
                self.startx == startx and self.starty == starty:
            return True

        self.visited[startx][starty] = True
        for i in range(4):
            new_startx = self.direction[i][0] + startx
            new_starty = self.direction[i][1] + starty

            if self._is_in_area(new_startx, new_starty)\
                and not self.visited[new_startx][new_starty]:
                print("进入循环", startx, starty, i, new_startx, new_starty)
                re = self._num_is_lands(grid, new_startx, new_starty)
                print("出入循环", startx, starty, i, new_startx, new_starty, re)

        return True

    def _is_in_area(self, startx, starty):
        return startx >= 0 and startx < self.grid_rows \
               and starty >= 0 and starty < self.grid_columns


class Solution1:
    def __init__(self):
        self.grid_rows = None
        self.grid_columns = None
        # 上 下 左 右 四个方向
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.startx = None
        self.starty = None
        self.visited = None

    def numIslands(self, grid):
        self.grid_rows = len(grid)
        if self.grid_rows == 0:
            return 0
        self.grid_columns = len(grid[0])
        self.visited = [[False for i in range(self.grid_columns)] for j in range(self.grid_rows)]
        res = 0
        for i in range(self.grid_rows):
             for j in range(self.grid_columns):
                if not self.visited[i][j] and grid[i][j] == '1':
                    res += 1
                    self.startx = i
                    self.starty = j
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, startx, starty):

        self.visited[startx][starty] = True
        for i in range(4):
            new_startx = self.direction[i][0] + startx
            new_starty = self.direction[i][1] + starty

            if self._is_in_area(new_startx, new_starty) \
                    and not self.visited[new_startx][new_starty]\
                    and grid[new_startx][new_starty] == '1':

                self.dfs(grid, new_startx, new_starty)

        return

    def _is_in_area(self, startx, starty):
        return startx >= 0 and startx < self.grid_rows \
               and starty >= 0 and starty < self.grid_columns



class Solution3:
    def __init__(self):
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.rows = 0
        self.cols = 0
        self.visited = None
    def numIslands(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[False for i in range(self.cols)] for j in range(self.rows)]
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1" and self.visited[i][j] == False:
                    self._num_is_lands(grid, i, j)
                    count += 1
        return count

    def _num_is_lands(self, grid, start_x, start_y):
        self.visited[start_x][start_y] = True
        for direction in self.direction:
            new_start_x = start_x + direction[0]
            new_start_y = start_y + direction[1]
            if self._isarea(new_start_x, new_start_y) \
                and self.visited[new_start_x][new_start_y] == False \
                and grid[new_start_x][new_start_y] == "1":
                self._num_is_lands(grid, new_start_x, new_start_y)

        return

    def _isarea(self, x, y):
        if x >= 0 and x < self.rows and y >= 0 and y < self.cols:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution3()
    '''
    11000
    11000
    00100
    00011
    '''
    # grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    re = so.numIslands(grid)
    print(re)