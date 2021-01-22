import math
class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        memo = [0 for i in range(num + 1)]
        memo[0] = 0
        memo[1] = 1
        for i in range(2, num+1):
            res = self.calculate(i)
            if res == 0:
                memo[i] = 1
            else:
                memo[i] = memo[res] + 1
        return memo

    # def calculate(self, x):
    #     i = 0
    #     while x > pow(2, i):
    #         i += 1
    #     if pow(2, i) == x:
    #         return 0
    #     res = x - pow(2, i-1)
    #     return res

    def calculate(self, x):
        int_base = int(math.log(x, 2))
        pow_x = pow(2, int_base)
        if pow_x == x:
            return 0
        return int(x - pow_x)


if __name__ == '__main__':
    so = Solution()
    re = so.countBits(9)
    print(re)