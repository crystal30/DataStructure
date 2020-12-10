# 这个方法超时哦
class Solution:
    def __init__(self):
        self.memo = None
    def lengthOfLIS(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums

        self.memo = [dict() for _ in range(len_nums)]
        return self.__length_of_lts(len_nums-1, nums, 0.5)


    def __length_of_lts(self, index, nums, lts):
        if index < 0:
            return 0

        if lts in self.memo[index].keys():
            return self.memo[index][lts]

        res = self.__length_of_lts(index-1, nums, lts)
        nums_index = nums[index]
        if lts == 0.5 or lts > nums_index:
            res = max(res, 1+self.__length_of_lts(index-1, nums, nums_index))

        self.memo[index][lts] = res
        return res


# 这个方法仍然没有第一次做的方法用时间少哦
class Solution1:
    def lengthOfLIS(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums == 1:
            return 1

        memo = [dict() for _ in range(len_nums)]
        nums_0 = nums[0]
        memo[0][None] = 1
        for i in range(1, len_nums):
            nums_i = nums[i]
            if nums_i > nums_0:
                memo[0][nums_i] = 1
            else:
                memo[0][nums_i] = 0

        for i in range(1, len_nums):
            nums_i = nums[i]
            memo[i][None] = max(memo[i-1][None], 1+memo[i-1][nums_i])
            for j in range(i+1, len_nums):
                nums_j = nums[j]
                if nums_i < nums_j:
                    memo[i][nums_j] = max(memo[i-1][nums_j], 1+memo[i-1][nums_i])
                else:
                    memo[i][nums_j] = memo[i - 1][nums_j]

        return max(memo[len_nums-1].values())

class Solution2:
    def lengthOfLIS(self, nums):
        len_nums = len(nums)
        if len_nums <= 0:
            return len_nums

        memo = [1 for i in range(len_nums)]
        for i in range(1,len_nums):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], 1+memo[j])

        return max(memo)


if __name__ == "__main__":
    so = Solution2()
    nums = [10,9,2,5,3,7,101,18]
    re = so.lengthOfLIS(nums)
    print(re)


