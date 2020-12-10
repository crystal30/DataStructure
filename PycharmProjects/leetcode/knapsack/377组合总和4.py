# 递归的方法
class Solution:
    def __init__(self):
        self.memo = None
    def combinationSum4(self, nums, target):
        len_nums = len(nums)
        if len_nums == 0 or target == 0:
            return 0

        min_num = min(nums)
        if min_num > target:
            return 0

        self.memo = [-1 for _ in range(target+1)]
        return self.combination_sum(nums, target)

    def combination_sum(self, nums, target):
        if target == 0:
            return 1

        if self.memo[target] != -1:
            return self.memo[target]

        self.memo[target] = sum([self.combination_sum(nums, target-num) for num in nums if num <= target])
        return self.memo[target]


# 动态规划的方法
class Solution1:
    def combinationSum4(self, nums, target):
        if len(nums) == 0 or target == 0:
            return 0
        if min(nums) > target:
            return 0
        memo = [0 for _ in range(target+1)]
        memo[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    memo[i] += memo[i-num]

        return memo[target]



# 动态规划, 你一步优化
class Solution2:
    def combinationSum4(self, nums, target):
        if len(nums) == 0 or target == 0:
            return 0
        if min(nums) > target:
            return 0
        memo = [0 for _ in range(target+1)]
        memo[0] = 1

        for i in range(1, target+1):
            memo[i] = sum([memo[i-num] for num in nums if num <= i])

        return memo[target]


if __name__ == "__main__":
    so = Solution2()
    nums = [1,2,3]
    target = 4
    re = so.combinationSum4(nums, target)
    print(re)