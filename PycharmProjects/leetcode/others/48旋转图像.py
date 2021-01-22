class Solution:
    def __init__(self):
        self.visited = None
        self.n = 0
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.visited = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if self.visited[i][j] is False:
                    matrix = self._rorate(i, j, matrix[i][j], matrix)
        return matrix

    def _rorate(self, start_i, start_j, e, matrix):
        new_i = start_j
        new_j = self.n - 1 - start_i
        if self.visited[new_i][new_j] is True:
            return matrix

        self.visited[new_i][new_j] = True
        temp = matrix[new_i][new_j]
        matrix[new_i][new_j] = e
        return self._rorate(new_i, new_j, temp, matrix)


if __name__ == "__main__":
    so = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    re = so.rotate(matrix)
    print(re)


