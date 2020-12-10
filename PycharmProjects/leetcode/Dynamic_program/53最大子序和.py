from copy import copy
class Solution:
    def maxSubArray(self, nums):
        len_nums = len(nums)
        # 根据题意，数组部位空
        if len_nums == 1:
            return nums[0]

        # memo[i][j]存储的是nums[i,j]（左闭右闭）的和
        memo = [[None for _ in range(len_nums)] for _ in range(len_nums)]
        for index, num in enumerate(nums):
            memo[index][index] = num
        re = copy(nums)
        for i in range(len_nums-2, -1, -1):
            for j in range(i+1, len_nums):
                if j - i + 1 <= 2:
                    memo[i][j] = nums[i] + nums[j]
                else:
                    memo[i][j] = nums[i] + nums[j] + memo[i+1][j-1]
                re.append(memo[i][j])
        return max(re)

# 贪心算法 和 滑动窗口
class Solution1:
    def maxSubArray(self, nums):
        # 根据题意，其长度不为0
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        pre_sum = nums[0]
        max_sum = nums[0]
        for index, num in enumerate(nums[1:]):
            if pre_sum <= 0:
                pre_sum = num
                max_sum = max(num, max_sum)
            else:
                pre_sum = pre_sum + num
                max_sum = max(max_sum, pre_sum)

        return max_sum


if __name__ == "__main__":
    so = Solution1()
    nums = [-2,1,-3,5,0]
    re = so.maxSubArray(nums)
    print(re)