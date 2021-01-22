class Solution:
    def __init__(self):
        self.visited = None
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 上，右，下，左
        self.row_num = 0
        self.col_num = 0
    def maxAreaOfIsland(self, grid):
        self.row_num = len(grid)
        if self.row_num == 0:
            return 0
        self.col_num = len(grid[0])
        self.visited = [[False for _ in range(self.col_num)] for _ in range(self.row_num)]
        max_area = 0
        for i in range(self.row_num):
            for j in range(self.col_num):
                if grid[i][j] == 1 and self.visited[i][j] is False:
                    area = self._area_of_is_land(i, j, grid)
                    if area > max_area:
                        max_area = area

        return max_area

    def _area_of_is_land(self, start_i, start_j, grid):
        # 终止条件？
        self.visited[start_i][start_j] = True
        area = 1
        for dir in self.direction:
            new_start_i = start_i + dir[0]
            new_start_j = start_j + dir[1]
            if self._is_area(new_start_i, new_start_j) \
                    and self.visited[new_start_i][new_start_j] is False \
                    and grid[new_start_i][new_start_j] == 1:
                area += self._area_of_is_land(new_start_i, new_start_j, grid)
        return area

    def _is_area(self, x, y):
        return 0 <= x < self.row_num and 0 <= y < self.col_num


if __name__ == "__main__":
    so = Solution()
 #    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 # [0,0,0,0,0,0,0,1,1,1,0,0,0],
 # [0,1,1,0,1,0,0,0,0,0,0,0,0],
 # [0,1,0,0,1,1,0,0,1,0,1,0,0],
 # [0,1,0,0,1,1,0,0,1,1,1,0,0],
 # [0,0,0,0,0,0,0,0,0,0,1,0,0],
 # [0,0,0,0,0,0,0,1,1,1,0,0,0],
 # [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[0,0,0,0,0,0,0,0]]

    re = so.maxAreaOfIsland(grid)
    print(re)




