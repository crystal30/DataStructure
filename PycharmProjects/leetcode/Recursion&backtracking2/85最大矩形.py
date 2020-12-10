# encoding:utf-8
# 该题目和84题(柱状图中最大矩形)，有异曲同工之处
# 递归与动态规划
class Solution:
    def __init__(self):
        self.row_num = 0
        self.col_num = 0
        self.width = None
        self.area = None

    def maximalRectangle(self, matrix):
        self.row_num = len(matrix)
        if self.row_num == 0:
            return 0
        self.col_num = len(matrix[0])
        self.width = [[0 for _ in range(self.col_num)] for _ in range(self.row_num)]
        self.area = [[0 for _ in range(self.col_num)] for _ in range(self.row_num)]
        for i in range(self.row_num):
            for j in range(self.col_num):
                if matrix[i][j] == "1" and self.width[i][j] == 0:
                        self.width[i][j] = self._max_right_range(matrix, i, j)

        self.area[0] = self.width[0][::]
        for i in range(1, self.row_num):
            for j in range(self.col_num):
                self.area[i][j] = self._max_area(i, j)

        return max((max(e) for e in self.area))

    def _max_right_range(self, matrix, start_i, start_j):
        if self.width[start_i][start_j] != 0:
            return self.width[start_i][start_j]

        if start_j == self.col_num - 1:
            self.width[start_i][start_j] = 1
            return 1

        if matrix[start_i][start_j + 1] == "1":
            width = 1 + self._max_right_range(matrix, start_i, start_j + 1)
            self.width[start_i][start_j] = width
            return width
        else:
            self.width[start_i][start_j] = 1
            return 1

    def _max_area(self, end_i, end_j):
        min_width = self.width[end_i][end_j]
        max_area = min_width
        for i in range(1, end_i+1):
            min_width = min(min_width, self.width[end_i-i][end_j])
            if min_width == 0:
                break
            max_area = max(max_area, min_width * (i + 1))

        return max_area



if __name__ == "__main__":
    so = Solution()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    # matrix = [["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["1","1","1","1","0"]]
    # matrix = [["0","1"],["1","0"]]
    # matrix = [["1", "1"]]
    re = so.maximalRectangle(matrix)
    print(re)




