from copy import deepcopy
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        if self.m == 0:
            return board
        self.n = len(board[0])
        board_copy = deepcopy(board)
        direction = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]  # 左上，上，右上，右，右下，下，左下，左
        # direction 这里需要验证一下

        for i in range(self.m):
            for j in range(self.n):
                life_count = 0
                for dir in direction:
                    new_i = i + dir[0]
                    new_j = j + dir[1]
                    if self.is_area(new_i, new_j) and board_copy[new_i][new_j] == 1:
                        life_count += 1

                if board_copy[i][j] == 0:
                    if life_count == 3:
                        board[i][j] = 1
                else:
                    if life_count < 2 or life_count > 3:
                        board[i][j] = 0

    def is_area(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

if __name__ == '__main__':
    so = Solution()
    board = [[1,1],[1,0]]
    so.gameOfLife(board)
    print(board)







