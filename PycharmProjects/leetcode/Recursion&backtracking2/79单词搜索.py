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


if __name__ == "__main__":
    so = Solution()
    board =[['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']]

    word = "D"
    re = so.exist(board, word)
    print(re)



