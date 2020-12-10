# coding:utf-8
class Solution:
    def rob(self, nums):
        len_nums = len(nums)
        memo = [-1] * len_nums
        return self.try_rob(nums, len_nums, 0, memo)

    def try_rob(self, nums, len_nums, start, memo):
        if start >= len_nums:
            return 0

        if memo[start] != -1:
            return memo[start]

        res = -1
        for i in range(start, len_nums):
            res = max(res, nums[i] + self.try_rob(nums, len_nums, i+2, memo))

        memo[start] = res
        return res

# 动态规划的思路
class Solution1:
    def rob(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        if len_nums <= 2:
            return max(nums)

        # memo[i] 表示从 nums[i:]打家抢舍获取的最大财富（必须是从i偷取）
        memo = [-1] * len_nums
        memo[-1] = nums[-1]
        memo[-2] = nums[-2]

        for i in range(3, len_nums+1):
            memo[len_nums - i] = nums[len_nums - i] + max(memo[len_nums - i + 2 :])

        return max(memo)

class Solution3:
    def __init__(self):
        self.memo = None
        self.len_nums = 0
    def rob(self, nums):
        self.len_nums = len(nums)
        if self.len_nums == 0:
            return 0
        if self.len_nums <= 1:
            return max(nums)

        self.memo = [-1 for i in range(self.len_nums)]
        max_money = -1
        for i in range(self.len_nums):
            money_i = self._rob(nums, i)
            if max_money < money_i:
                max_money = money_i

        return max_money


    def _rob(self, nums, start_i):
        if self.memo[start_i] != -1:
            return self.memo[start_i]

        if start_i + 2 >= self.len_nums:
            self.memo[start_i] = nums[start_i]
            return self.memo[start_i]

        money_list = []
        for i in range(start_i+2, self.len_nums):
            money_list.append(self._rob(nums, i))

        self.memo[start_i] = nums[start_i] + max(money_list)
        return self.memo[start_i]


class Solution5:
    def rob(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums <= 1:
            return max(nums)

        memo = [-1 for _ in range(len_nums)]
        memo[-1] = nums[-1]
        memo[-2] = nums[-2]

        nums_list = [_ for _ in range(len_nums-2)]
        for i in nums_list[::-1]:
            money_list = []
            for j in range(i+2, len_nums):
                money_list.append(memo[j])
            memo[i] = nums[i] + max(money_list)

        return max(memo)


if __name__ == "__main__":
    so = Solution5()
    nums = [2, 1, 1, 2]
    re = so.rob(nums)
    print(re)


