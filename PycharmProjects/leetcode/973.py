class Solution:
    def swimInWater(self, grid):
        len_grid = len(grid)
        i = len_grid - 1
        j = len_grid - 1
        re = grid[i][j]
        history = []
        source_min_dep = grid[i][j]
        while i >= 0 and j >= 0:
            # 要遍历左，右，上

            # 没有左，上
            if i == 0 and j == 0:
                min_deep = -1
                x = i - 1
                y = j - 1

            # 没有 左,  只有右和上
            elif j == 0 and [i-1, j] not in history:
                # 有右
                if j + 1 < len_grid and [i, j+1] not in history:
                    min_deep, x, y = self.compare_grid(i, j + 1, i - 1, j, grid)
                # 没有右
                else:
                    min_deep = grid[i - 1][j]
                    x = i - 1
                    y = j

            # 没有左，没有上，只可能有右
            elif j == 0 and [i-1, j] in history:
                # 有右
                if j + 1 < len_grid and [i, j + 1] not in history:
                    min_deep = grid[i][j+1]
                    x = i
                    y = j+1

                else:
                    min_deep = -1
                    x = -1
                    y = -1

            # 没有 上,  只有左和右
            elif i == 0 and [i, j-1] not in history:
                # 有右
                if j + 1 < len_grid and [i, j+1] not in history:
                    min_deep, x, y = self.compare_grid(i, j + 1, i, j - 1, grid)
                # 没有右
                else:
                    min_deep = grid[i][j - 1]
                    x = i
                    y = j - 1

            # 没有上和左，只可能有右
            elif i == 0 and [i, j - 1] in history:
                # 有右
                if j + 1 < len_grid and [i, j + 1] not in history:
                    min_deep = grid[i][j + 1]
                    x = i
                    y = j + 1
                else:
                    min_deep = -1
                    x = -1
                    y = -1

            else: # 有左，上 i ！= 0 and j != 0
                # 有 左，右，上
                if [i, j - 1] not in history and [i-1, j] not in history:
                    if j + 1 < len_grid and [i, j+1] not in history:
                        min_deep, x, y = self.compare_grid(i, j + 1, i, j - 1, grid)
                        min_deep, x, y = self.compare_grid(x, y, i - 1, j, grid)
                    # 没有右，有左，上
                    else:
                        min_deep, x, y = self.compare_grid(i-1, j, i, j-1, grid)
                # 有左，右
                elif [i, j - 1] not in history:
                    # 有右
                    if j + 1 < len_grid and [i, j + 1] not in history:
                        min_deep, x, y = self.compare_grid(i, j - 1, i, j+1, grid)
                    # 没有右
                    else:
                        min_deep = grid[i][j-1]
                        x = i
                        y = j-1
                else: # 有上 右
                    # 有右
                    if j + 1 < len_grid and [i, j + 1] not in history:
                        min_deep, x, y = self.compare_grid(i-1, j, i, j + 1, grid)
                    # 没有右
                    else:
                        min_deep = grid[i-1][j]
                        x = i - 1
                        y = j


            if min_deep > source_min_dep:
                re += min_deep - source_min_dep
                source_min_dep = min_deep

            history.append([i, j])
            i = x
            j = y
        return re

    def compare_grid(self, r_x, r_y, b_x, b_y, grid):
        if grid[r_x][r_y] >= grid[b_x][b_y]:
            return grid[b_x][b_y], b_x, b_y
        if grid[r_x][r_y] < grid[b_x][b_y]:
            return grid[r_x][r_y], r_x, r_y

if __name__ == "__main__":
    so = Solution()
    grid = [[11,15,3,2],[6,4,0,13],[5,8,9,10],[1,14,12,7]]
    re = so.swimInWater(grid)
    print(re)
