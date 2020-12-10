class Solution:
    def minimumTotal(self, triangle):
        len_triangle = len(triangle)
        if len_triangle == 0:
            return 0
        if len_triangle == 1:
            return triangle[0][0]

        for i in range(1, len_triangle):
            for j in range(i+1):

                # 当元素为三角形的左边缘时
                if j == 0:
                    triangle[i][0] += triangle[i-1][0]
                    continue
                # 当元素为三角形的右边缘时
                if j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                    continue

                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

        return min(triangle[len_triangle - 1])

from copy import copy
class Solution2:
    def minimumTotal(self, triangle):
        n = len(triangle)
        if n == 0:
            return 0

        memo = copy(triangle)
        row_list = [i for i in range(n-1)]
        for row in row_list[::-1]:
            for col in range(row+1):
                memo[row][col] += min(memo[row+1][col], memo[row+1][col+1])

        return memo[0][0]



if __name__ == "__main__":
    so = Solution2()
    triangle = [[2],[3,4],[6,7,5],[4,1,8,3]]
    re = so.minimumTotal(triangle)
    print(re)





























