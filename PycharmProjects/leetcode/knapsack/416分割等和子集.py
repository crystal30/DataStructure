from copy import copy

# 该方法超时，可不可以用记忆的方法，减少时间
class Solution:
    def __init__(self):
        self.par_nums = []
        self.len_nums = 0
    def canPartition(self, nums):
        sum_nums = sum(nums)
        # 因为是非空的数组，所以不用考虑len_nums = 0的情况
        self.len_nums = len(nums)
        if self.len_nums == 1 or sum_nums % 2 == 1:
            return False

        target = sum_nums // 2
        nums.sort()
        # 返回 nums[0:]中和为targrt的元素，若没有，则返回空
        re_bool = self.partition(nums, 0, target, [])
        par_anthor_nums = [nums[i] for i in range(self.len_nums) if i not in self.par_nums]
        if re_bool and sum(par_anthor_nums) == target:
            return True
        else:
            return False

    def partition(self, nums, start_i, target, re):
        """

        :param nums: nums为排好序的
        :param target:
        :param re:
        :return:
        """
        if target == 0:
            self.par_nums = copy(re)
            return True

        for i in range(start_i, self.len_nums):
            e = nums[i]
            if e <= target:
                re.append(i)
                if self.partition(nums, i+1, target-e, re):
                    return True
                re.pop()
            else:
                break

        return False

# 自上而下，递归的思路
class Solution1:
    def __init__(self):
        self.memo = None
    def canPartition(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        par_sum_nums = sum_nums // 2
        self.memo = [[-1 for _ in range(par_sum_nums+1)] for _ in range(len(nums))]
        return self.partition(nums, len(nums)-1, par_sum_nums)

    def partition(self, nums, index, par_sum_nums):
        """
        nums[0:index] 可以填满 par_sum_nums
        :param nums:
        :param index:
        :param par_sum_nums:
        :return:
        """
        if par_sum_nums == 0:
            return True

        if par_sum_nums <0 or index < 0:
            return False

        if self.memo[index][par_sum_nums] != -1:
            return self.memo[index][par_sum_nums]

        self.memo[index][par_sum_nums] = \
            self.partition(nums, index-1, par_sum_nums) \
           or self.partition(nums, index-1, par_sum_nums-nums[index])

        return self.memo[index][par_sum_nums]


# 自上而下，动态规划的思路
class Solution1:
    def canPartition(self, nums):
        len_nums = len(nums)

        # 题目中已经说明为非空数组
        if len_nums == 1:
            return False

        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        par_sum_nums = sum_nums // 2
        memo = [[_ for _ in range(par_sum_nums+1)] for _ in range(len_nums)]

        for j in range(par_sum_nums+1):
            memo[0][j] = nums[0] == j

        for i in range(1, len_nums):
            for j in range(par_sum_nums+1):
                memo[i][j] = memo[i-1][j]
                if j - nums[i] > 0:
                    memo[i][j] = memo[i][j] or memo[i-1][j-nums[i]]
                elif j - nums[i] == 0:
                    memo[i][j] = True

        return memo[len_nums-1][par_sum_nums]


# 自上而下，动态规划的思路
# 空间复杂度的改进

class Solution2:
    def canPartition(self, nums):
        len_nums = len(nums)

        # 题目中已经说明为非空数组
        if len_nums == 1:
            return False

        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False

        par_sum_nums = sum_nums // 2
        memo = [False for _ in range(par_sum_nums+1)]

        for j in range(par_sum_nums+1):
            memo[j] = nums[0] == j

        for i in range(1, len_nums):
            for j in range(par_sum_nums, -1, -1):
                res = memo[j]
                if j - nums[i] > 0:
                    res = res or memo[j-nums[i]]
                elif j - nums[i] == 0:
                    res = True
                memo[j] = res

        return memo[par_sum_nums]



if __name__ == "__main__":
    so = Solution1()
    nums = [1,1,1,1]
    re = so.canPartition(nums)
    print(re)