class Solution:
    def __init__(self):

        self.direction = [[-1, 0], [0, -1],[0, 1], [1, 0]]
        self.m = None
        self.n = None
        self.to_pacitic = False
        self.to_atlantic = False
        self.visited = None

    def pacificAtlantic(self, matrix):
        res = []
        self.m = len(matrix)
        if self.m == 0:
            return res

        self.n = len(matrix[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.res = [[[False, False] for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j]:
                    self.dfs(matrix, i, j)

                if self.res[i][j][0] and self.res[i][j][1]:
                    res.append([i, j])
        return res


    def dfs(self, matrix, startx, starty):

        self.visited[startx][starty] = True
        if startx == 0 or starty == 0:
            # 流向太平洋
            self.res[startx][starty][0] = True

        if startx == self.m - 1 or starty == self.n - 1:
            # 流向大西洋
            self.res[startx][starty][1] = True

        if self.res[startx][starty][0] and self.res[startx][starty][1]:
            return True, True

        h = matrix[startx][starty]

        for i in range(4):
            new_startx = startx + self.direction[i][0]
            new_starty = starty + self.direction[i][1]

            if self.is_area(new_startx, new_starty) \
                    and h >= matrix[new_startx][new_starty]:
                if not self.visited[new_startx][new_starty]:
                    to_p, to_a = self.dfs(matrix, new_startx, new_starty)
                    if to_p:
                        self.res[startx][starty][0] = True
                    if to_a:
                        self.res[startx][starty][1] = True

                else:
                    if self.res[new_startx][new_starty][0] == True:
                        self.res[startx][starty][0] = True
                    if self.res[new_startx][new_starty][1] == True:
                        self.res[startx][starty][1] = True
        return self.res[startx][starty][0], self.res[startx][starty][1]

    def is_area(self, startx, starty):
        return startx >= 0 and startx < self.m \
               and starty >= 0 and starty < self.n


class Solution3:
    def __init__(self):
        self.row_num = 0
        self.col_num = 0
        self.visited = None
        self.res = None
        self.direction = [[0,-1], [-1, 0], [0, 1], [1, 0]] # 左，上, 右，下

    def pacificAtlantic(self, matrix):
        result = []
        self.row_num = len(matrix)
        if self.row_num == 0:
            return []
        self.col_num = len(matrix[0])
        self.visited = [[False for _ in range(self.col_num)] for _ in range(self.row_num)]
        self.res = [[[False, False] for _ in range(self.col_num)] for _ in range(self.row_num)]

        for i in range(self.row_num):
            for j in range(self.col_num):
                if not self.visited[i][j]:
                    self._pac_atl(matrix, i, j)
                if self.res[i][j][0] and self.res[i][j][1]:
                    result.append([i, j])

        return result

    def _pac_atl(self, matrix, x, y):
        self.visited[x][y] = True
        # 流向太平洋
        if x == 0 or y == 0:
            self.res[x][y][0] = True

        # 流向大西洋
        if x == self.row_num-1 or y == self.col_num-1:
            self.res[x][y][1] = True

        if self.res[x][y][0] and self.res[x][y][1]:
            return True, True

        e = matrix[x][y]
        for dir in self.direction:
            new_x = x + dir[0]
            new_y = y + dir[1]
            if self._is_area(new_x, new_y) and e >= matrix[new_x][new_y]:
                if not self.visited[new_x][new_y]:
                    to_p, to_a = self._pac_atl(matrix, new_x, new_y)
                    if to_p:
                        self.res[x][y][0] = True
                    if to_a:
                        self.res[x][y][1] = True
                else:
                    if self.res[new_x][new_y][0]:
                        self.res[x][y][0] = True
                    if self.res[new_x][new_y][1]:
                        self.res[x][y][1] = True
        return self.res[x][y][0], self.res[x][y][1]


    def _is_area(self, x, y):
        return x >= 0 and x < self.row_num \
               and y >= 0 and y < self.col_num



if __name__ == "__main__":
    so = Solution3()
    matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # matrix = [[1,2,3],[8,9,4],[7,6,5]]
    matrix1 = [[10,10,10],[10,1,10],[10,10,10]]
    matrix2 = [[10,10,1,11,2,15,17,6,17,10,0,10,18,9,16,13,8,9,12,6,3,2,5,19,4,14],
                [12,19,13,2,7,2,3,8,17,4,2,1,8,13,7,2,10,16,12,3,4,12,4,16,0,12],
                [1,12,9,18,12,16,17,5,13,0,7,13,12,13,6,2,11,19,7,2,6,11,11,0,17,6],
                [1,12,2,0,11,7,7,3,7,13,11,1,11,15,5,13,14,12,4,10,5,16,3,17,18,12],
                [9,16,11,5,9,13,7,18,18,14,19,10,9,4,8,14,4,19,13,1,14,8,0,3,12,10],
                [10,19,9,11,1,18,1,2,1,8,1,5,2,15,14,13,18,18,11,4,15,3,15,12,12,2],
                [0,10,9,2,15,9,12,7,0,0,12,18,9,12,18,4,18,10,3,1,17,14,13,18,9,4],
                [3,19,9,16,16,19,11,19,6,9,18,0,12,11,13,1,15,6,9,18,9,6,3,12,12,2],
                [0,16,15,12,3,19,18,9,5,1,4,3,19,15,1,0,7,10,14,4,8,10,15,16,14,8],
                [15,9,3,15,19,17,17,10,9,8,16,11,3,15,15,9,1,14,11,13,16,7,1,7,13,5],
                [9,19,6,7,19,14,4,18,6,10,19,13,12,7,7,15,6,10,7,8,8,8,19,13,17,14],
                [14,7,1,15,2,6,12,4,2,19,17,17,8,9,19,10,0,12,4,12,4,16,15,18,8,0],
                [4,8,5,8,0,2,19,18,1,7,13,9,13,16,6,15,15,12,18,5,8,11,6,17,5,11],
                [17,16,9,19,12,6,13,19,0,6,7,9,7,13,9,18,5,15,16,8,18,9,6,0,11,14],
                [11,5,13,3,12,19,5,15,2,15,9,16,6,12,8,0,19,19,11,0,16,8,15,15,1,12],
                [15,16,16,19,14,1,2,11,14,8,16,13,2,0,3,8,1,5,4,15,12,5,13,3,5,3]]
    re = so.pacificAtlantic(matrix)
    print(re)

