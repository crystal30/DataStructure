class Solution:
    def __init__(self):
        self.board_rows = None
        self.board_columns = None
        # 上，右，下，左
        self.search_direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def exist(self, board, word):
        self.board_rows = len(board)
        self.board_columns = len(board[0])
        board_visited = [[False for _ in range(self.board_columns)]
                         for _ in range(self.board_rows)]

        for i in range(self.board_rows):
            for j in range(self.board_columns):
                if (self._word_search(board, word, 0, i, j, board_visited)):
                    return True

        return False

    def _word_search(self, board, word, index, i, j, board_visited):
        if index == len(word) - 1:
            return board[i][j] == word[index]

        if board[i][j] == word[index]:
            board_visited[i][j] = True
            for k in range(4):
                new_i = self.search_direction[k][0] + i
                new_j = self.search_direction[k][1] + j
                if self.ij_isvaild(new_i, new_j) and not board_visited[new_i][new_j]:
                    re = self._word_search(board, word, index+1, new_i, new_j, board_visited)
                    if re:
                        return True

            board_visited[i][j] = False
        return False

    def ij_isvaild(self, i, j):
        return i >= 0 and i < self.board_rows and j >= 0 and j < self.board_columns

class Solution2:
    def __init__(self):
        self.row_num = 0
        self.col_num = 0
        self.visited = None
        self.direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def exist(self, board, word):
        self.row_num = len(board)
        self.col_num = len(board[0])
        self.visited = [[False for i in range(self.col_num)] for j in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                if self._exist(board, word, i, j, 0):
                    return True

        return False


    def _exist(self, board, word, start_x, start_y, i):
        if i < len(word) and board[start_x][start_y] != word[i]:
            return False
        if i == len(word) -1 and board[start_x][start_y] == word[i]:
            return True

        self.visited[start_x][start_y] = True
        for dire in self.direction:
            new_start_x = start_x + dire[0]
            new_start_y = start_y + dire[1]
            if self._isarea(new_start_x, new_start_y) \
                    and self.visited[new_start_x][new_start_y]==False:
                if self._exist(board, word, new_start_x, new_start_y, i+1):
                    return True
        self.visited[start_x][start_y] = False
        return False


    def _isarea(self, x, y):
        if x < self.row_num and x >= 0 and y<self.col_num and y >= 0:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution2()
    # board =[['A', 'B', 'C', 'E'],
    #         ['S', 'F', 'C', 'S'],
    #         ['A', 'D', 'E', 'E']]
    board = [["A"]]

    word = "A"
    re = so.exist(board, word)
    print(re)



