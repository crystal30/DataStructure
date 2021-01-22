# coding : utf-8
# 该方法超出时间限制
class Solution:
    def removeKdigits(self, num: str, k: int):
        len_num = len(num)
        return self._remove_k_digits(num, len_num-1, k)

    def _remove_k_digits(self, num, index, k):
        # 循环结束的条件？
        if index+1 == k:
            return "0"
        if k == 0:
            return num[:index+1]

        re1 = int(self._remove_k_digits(num, index-1, k-1))
        re2 = int(self._remove_k_digits(num, index-1, k) + num[index])
        return str(min(re1, re2))


# 用记忆化搜索的方式，仍然超出时间限制
class Solution1:
    def __init__(self):
        self.memo = None
    def removeKdigits(self, num: str, k: int):
        len_num = len(num)
        # 存储num[0:index]前闭后闭，删除k个元素的最小值
        self.memo = [[None for _ in range(k+1)] for _ in range(len_num)]
        return self._remove_k_digits(num, len_num-1, k)

    def _remove_k_digits(self, num, index, k):
        if index+1 == k:
            self.memo[index][k] = '0'
            return "0"
        if k == 0:
            self.memo[index][0] = num[:index+1]
            return num[:index+1]

        if self.memo[index][k] is not None:
            return self.memo[index][k]

        re1 = int(self._remove_k_digits(num, index-1, k-1))
        re2 = int(self._remove_k_digits(num, index-1, k) + num[index])
        return str(min(re1, re2))

# 用动态规划的方法, 仍然超出时间限制
class Solution2:
    def removeKdigits(self, num: str, k: int):
        len_num = len(num)
        # 存储num[0:index]前闭后闭，删除k个元素的最小值
        memo = [[None for _ in range(k+1)] for _ in range(len_num)]
        for i in range(len_num):
            memo[i][0] = num[:i+1]
            if i+1 <= k:
                memo[i][i+1] = "0"

        for i in range(1, len_num):
            for j in range(1, k+1):
                if j > i:
                    memo[i][j] = "0"
                else:
                    memo[i][j] = str(min(int(memo[i-1][j-1]), int(memo[i-1][j] + num[i])))

        return memo[len_num-1][k]

# 用动态规划的方法,开始不变为str，最后再统一变str,仍然超出时间限制
class Solution3:
    def removeKdigits(self, num: str, k: int):
        len_num = len(num)
        # 存储num[0:index]前闭后闭，删除k个元素的最小值
        memo = [[None for _ in range(k+1)] for _ in range(len_num)]
        for i in range(len_num):
            memo[i][0] = int(num[:i+1])
            if i+1 <= k:
                memo[i][i+1] = 0

        for i in range(1, len_num):
            for j in range(1, k+1):
                if j > i:
                    memo[i][j] = 0
                else:
                    memo[i][j] = min(memo[i-1][j-1], memo[i-1][j]*10 + int(num[i]))

        return str(memo[len_num-1][k])


# 用贪心算法和栈
class Solution4:
    def removeKdigits(self, num: str, k: int):
        len_num = len(num)
        if len_num == k:
            return "0"
        if len_num == 0:
            return "0"
        if k == 0:
            return num

        stack = [num[0]]
        for i in range(1, len_num):
            while len(stack) > 0 and int(stack[-1]) > int(num[i]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])

        if k > 0:
            len_stack = len(stack)
            stack = stack[:len_stack-k]

        re = "".join(stack).lstrip("0")
        if len(re) == 0:
            return "0"
        else:
            return re

if __name__ == "__main__":
    so = Solution4()
    num = "2222111"
    k = 3
    re = so.removeKdigits(num, k)
    print(re)

