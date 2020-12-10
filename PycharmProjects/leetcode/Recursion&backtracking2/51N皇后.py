class Solution:
    def __init__(self):
        self.res = []
        self.row = []
        self.col = None
        self.dia1 = None
        self.dia2 = None

    def solveNQueens(self, n: int):
        if n == 0:
            return self.res

        self.col = [False for _ in range(n)]
        self.dia1 = [False for _ in range(2*n-1)]
        self.dia2 = [False for _ in range(2*n-1)]

        self._solve_n_queens(n, 0, [])
        return self.res

    def _solve_n_queens(self, n, index, row):
        if index == n:
            self.res.append(self.generate_board(n, row))
            return

        for i in range(n):
            if not self.col[i] and not self.dia1[index+i] and not self.dia2[index-i+n-1]:
                row.append(i)
                self.col[i] = True
                self.dia1[index + i] = True
                self.dia2[index - i + n - 1] = True
                self._solve_n_queens(n, index+1, row)
                row.pop()
                self.col[i] = False
                self.dia1[index + i] = False
                self.dia2[index - i + n - 1] = False
        return

    def generate_board(self, n, row):
        sub_res = []
        for i in range(n):
            Q_index = row[i]
            sub_res.append("."*(Q_index) + 'Q' + "."*(n-Q_index-1))
        return sub_res

if __name__ == "__main__":
    so = Solution()
    n = 4
    re = so.solveNQueens(n)
    print(re)