class Solution:
    def __init__(self):
        self.visited = None
        self.row_num = 0
        self.col_num = 0
        self.direction = [[0, 1], [1, 1], [1, 0]] # 右，斜，下

    def maximalSquare(self, matrix):
        self.row_num = len(matrix)
        self.col_num = len(matrix[0])

        self.visited = [[-1 for _ in range(self.col_num)] for _ in range(self.row_num)]
        re = [0]
        for i in range(self.row_num):
            for j in range(self.col_num):
                if matrix[i][j] == "1":
                    if self.visited[i][j] == -1:
                        re.append(self.__max_square(matrix, i, j))
                    else:
                        re.append(self.visited[i][j])

        max_re = max(re)
        return max_re * max_re


    def __max_square(self, matrix, start_i, start_j):

        if start_i == self.row_num-1 or start_j == self.col_num-1:
            self.visited[start_i][start_j] = 1
            return 1

        re = []
        for dir in self.direction:
            new_start_i = start_i + dir[0]
            new_start_j = start_j + dir[1]
            if matrix[new_start_i][new_start_j] == "1":
                if self.visited[new_start_i][new_start_j] != -1:
                    re.append(1 + self.visited[new_start_i][new_start_j])
                else:
                    re.append(1 + self.__max_square(matrix, new_start_i, new_start_j))
            else:
                re.append(1)
                break
        min_re = min(re)
        self.visited[start_i][start_j] = min_re
        return min_re


if __name__ == "__main__":
    so = Solution()
    matrix = [["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","0"]]
    # matrix = [["0","1"],["1","0"]]
    # matrix = [["1", "1"]]
    re = so.maximalSquare(matrix)
    print(re)




