class Solution:
    def __init__(self):
        self.res = []
        self.used = None
    def permuteUnique(self, nums):
        len_nums = len(nums)
        self.used = [False] * len_nums
        self.generationPermuteUnique(nums, 0, [])
        return list(self.res)

    # nums 即要求全排列的数组
    # index 目前temp中有多少个数字
    # temp
    def generationPermuteUnique(self, nums, index, temp):
        len_nums = len(nums)
        if index == len_nums:
            if temp not in self.res:
                self.res.append(temp.copy())
            return

        for i in range(len_nums):
            if self.used[i] == False:
                temp.append(nums[i])
                self.used[i] = True
                self.generationPermuteUnique(nums, index+1, temp)
                temp.pop()
                self.used[i] = False
        return

    # 用自己比较理解的第二种方法做一下
from copy import copy
class Solution1:
    def __init__(self):
        self.res = list()
        self.res_str = set()

    def permuteUnique(self, nums):
        len_nums = len(nums)
        visited_nums = [False] * len_nums
        self._pernute_unipue(nums, len_nums, visited_nums, [])
        return self.res

    def _pernute_unipue(self, nums, len_mums, visited_nums, sub_nums):
        if len(sub_nums) == len_mums:
            sub_nums_str_list = [str(e) for e in sub_nums]
            sub_nums_str = ''.join(sub_nums_str_list)
            if sub_nums_str not in self.res_str:
                self.res_str.add(sub_nums_str)
                self.res.append(copy(sub_nums))
            return

        for i in range(len_mums):
            if visited_nums[i] == False:
                sub_nums.append(nums[i])
                visited_nums[i] = True
                self._pernute_unipue(nums, len_mums, visited_nums, sub_nums)
                sub_nums.pop()
                visited_nums[i] = False

        return

if __name__ == "__main__":
    so = Solution1()
    nums = [1,1,2]
    re = so.permuteUnique(nums)
    print(re)

