# coding:utf-8
class Solution:
    def __init__(self):
        self.memo = None

    def findMaxForm(self, strs, m, n):
        len_strs = len(strs)
        if len_strs == 0:
            return 0
        self.memo = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len_strs)]

        return max(0, self.find_max_form(strs, len(strs)-1, m, n))

    def find_max_form(self, strs, index, m, n):

        if m == 0 and n == 0:
            return 0

        num_0 = 0
        num_1 = 0
        for e in strs[index]:
            if e == '0':
                num_0 += 1
            else:
                num_1 += 1

        if index == 0:
            if num_0 <= m and num_1 <= n:
                return 1
            else:
                return 0

        if self.memo[index][m][n] != -1:
            return self.memo[index][m][n]

        if m - num_0 >= 0 and n - num_1 >= 0:
            res = max(self.find_max_form(strs, index-1, m, n),
                      1+self.find_max_form(strs, index-1, m-num_0, n-num_1))
        else:
            res = self.find_max_form(strs, index-1, m, n)
        self.memo[index][m][n] = res
        return res


class Solution1:
    def findMaxForm(self, strs, m, n):
        len_strs = len(strs)
        memo = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len_strs)]

        zero_num, one_num = self.calculate_zero_one(strs[0])
        for j in range(m+1):
            for k in range(n+1):
                if zero_num <= j and one_num <= k:
                    memo[0][j][k] = 1

        for i in range(1, len_strs):
            zero_num, one_num = self.calculate_zero_one(strs[i])
            for j in range(m+1):
                for k in range(n+1):
                    if zero_num <= j and one_num <= k:
                        # print(i, k, j)
                        memo[i][j][k] = max(memo[i-1][j][k], 1+memo[i-1][j-zero_num][k-one_num])
                    else:
                        memo[i][j][k] = memo[i-1][j][k]

        return memo[len_strs-1][m][n]


    def calculate_zero_one(self, e):
        zero_num = 0
        one_num = 0
        for sub_e in e:
            if sub_e == '0':
                zero_num += 1
            else:
                one_num += 1
        return zero_num, one_num


if __name__ == "__main__":
    so = Solution1()
    strs = ["10"]
    m = 5
    n = 3
    re = so.findMaxForm(strs, m, n)
    print(re)