class Solution:
    def __init__(self):
        self.memo = None
    def findTargetSumWays(self, nums, S):
        len_nums = len(nums)
        self.memo = [dict() for _ in range(len_nums)]
        return self.__find_target_sum_ways(nums, S, len_nums-1)

    def __find_target_sum_ways(self, nums, S, index):
        if index == 0:
            nums_0 = nums[0]
            if S == nums_0 or S == -nums_0:
                return 1
            else:
                return 0

        if S in self.memo[index].keys():
            return self.memo[index][S]

        index_S = self.__find_target_sum_ways(nums, S-nums[index], index-1) + \
                  self.__find_target_sum_ways(nums, S+nums[index], index-1)

        self.memo[index][S] = index_S
        return index_S


if __name__ == "__main__":
    so = Solution()
    nums = [1, 1, 1, 1, 1]
    S = 3
    re = so.findTargetSumWays(nums, S)
    print(re)

