# coding: utf-8
class Solution:
    def __init__(self):
        self.rows = None
        self.columns = None
        self.visited = None
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        if not self.rows:
            return board

        self.columns = len(board[0])

        if self.rows <= 2 or self.columns <= 2:
            return board

        self.visited = [[False for _ in range(self.columns)] for _ in range(self.rows)]

        # i，j肯定在区域内，且不是边缘数据，
        for i in range(1, self.rows - 1):
            for j in range(1, self.columns - 1):
                if board[i][j] == "O" and not self.visited[i][j]:
                    self.dfs(board, i, j)

    def dfs(self, board, startx, starty):

        self.visited[startx][starty] = True
        board[startx][starty] = 'X'

        for i in range(4):
            new_startx = startx + self.direction[i][0]
            new_starty = starty + self.direction[i][1]

            # 判断new_startx, new_starty是否是有效的 在区域内，且不是边缘数据
            if self.is_area(new_startx, new_starty)\
                and board[new_startx][new_starty] == 'O':

                if not self.visited[new_startx][new_starty]:
                    if self.is_not_edge(new_startx, new_starty):

                        self.dfs(board, new_startx, new_starty)
                    else:
                        self.re_dfs(board, startx, starty)
                        return
                else:
                    self.re_dfs(board, startx, starty)
                    return
        return

    def re_dfs(self, board, startx, starty):

        board[startx][starty] = 'O'

        for i in range(4):
            new_startx = startx + self.direction[i][0]
            new_starty = starty + self.direction[i][1]

            # 注：self.visited[new_startx][new_starty] == True
            # new_startx, new_starty 就不会是边缘数据
            if self.is_area(new_startx, new_starty)\
                and self.visited[new_startx][new_starty]\
                and board[new_startx][new_starty] == 'X':

                self.re_dfs(board, new_startx, new_starty)
        return


    def is_not_edge(self, startx, starty):
        return startx > 0 and startx < self.rows - 1 \
               and starty > 0 and starty < self.columns - 1

    def is_area(self, startx, starty):
        return startx >= 0 and startx < self.rows\
               and starty >= 0 and starty < self.columns


class Solution2:
    def __init__(self):
        self.dire = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 上，右，下，左
        self.row_num = 0
        self.col_num = 0
        self.visited = None
    def solve(self, board) -> None:
        self.row_num = len(board)
        if self.row_num == 0:
            return board
        self.col_num = len(board[0])
        self.visited = [[False for _ in range(self.col_num)] for _ in range(self.row_num)]

        for i in [0, self.row_num-1]:
            for j in range(self.col_num):
                if not self.visited[i][j] and board[i][j] == 'O':
                    self._solve(board, i, j)
        for j in [0, self.col_num-1]:
            for i in range(1, self.row_num-1):
                if not self.visited[i][j] and board[i][j] == 'O':
                    self._solve(board, i, j)

        for i in range(1, self.row_num-1):
            for j in range(1, self.col_num-1):
                if not self.visited[i][j] and board[i][j] == 'O':
                    self._solve1(board, i, j)

    def _solve(self, board, start_x, start_y):
        self.visited[start_x][start_y] = True
        for dir in self.dire:
            new_start_x = start_x + dir[0]
            new_start_y = start_y + dir[1]
            if self._is_area(new_start_x, new_start_y) and \
                not self.visited[new_start_x][new_start_y] and \
                    board[new_start_x][new_start_y] == 'O':
                    self._solve(board, new_start_x, new_start_y)
        return

    def _solve1(self, board, start_x, start_y):
        self.visited[start_x][start_y] = True
        board[start_x][start_y] = 'X'
        for dir in self.dire:
            new_start_x = start_x + dir[0]
            new_start_y = start_y + dir[1]
            if self._is_area(new_start_x, new_start_y) and \
                not self.visited[new_start_x][new_start_y] and \
                    board[new_start_x][new_start_y] == 'O':
                    self._solve1(board, new_start_x, new_start_y)
        return


    def _is_area(self, x, y):
        if x >= 0 and x < self.row_num and y >= 0 and y < self.col_num:
            return True
        else:
            return False

    # def _is_adge(self, x, y):
    #     if x == 0 or x == self.row_num-1 or y == 0 or y == self.col_num-1:
    #         return True
    #     else:
    #         return False



if __name__ == "__main__":
    so = Solution2()
    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    # board1 = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "X", "O", "X"]]
    # board2 = [["O","X","O","O","O","O","O","O","O"],
    #           ["O","O","O","X","O","O","O","O","X"],
    #           ["O","X","O","X","O","O","O","O","X"],
    #           ["O","O","O","O","X","O","O","O","O"],
    #           ["X","O","O","O","O","O","O","O","X"],
    #           ["X","X","O","O","X","O","X","O","X"],
    #           ["O","O","O","X","O","O","O","O","O"],
    #           ["O","O","O","X","O","O","O","O","O"],
    #           ["O","O","O","O","O","X","X","O","O"]]
    so.solve(board)
    print(board)






