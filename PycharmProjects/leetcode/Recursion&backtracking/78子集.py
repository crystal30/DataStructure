class Solution:

    def subsets(self, nums):
        len_nums = len(nums)
        res = [[], [nums[0]]]

        for i in range(1, len_nums):
            sub_res = []
            for e in res:
                temp_e = e.copy()
                temp_e.append(nums[i])
                sub_res.append(temp_e.copy())
            res.extend(sub_res)
        return res

from copy import copy
class Solution1:
    def subsets(self, nums):
        return self._subset(nums, [[]])

    def _subset(self, nums, sub_re):
        len_nums = len(nums)
        if len_nums == 0:
            return sub_re

        for i in range(len_nums):
            temp = []
            for e in sub_re:
                new_e = copy(e)
                new_e.append(nums[i])
                temp.append(new_e)

            sub_re.extend(temp)
            sub_re = self._subset(nums[i+1:], sub_re)

            return sub_re


if __name__ == "__main__":
    so = Solution1()
    nums = [1,2,3]
    re = so.subsets(nums)
    print(re)