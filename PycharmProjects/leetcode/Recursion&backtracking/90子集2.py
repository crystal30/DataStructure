from collections import Counter
class Solution:
    def subsetsWithDup(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return [[]]

        res = [[], [nums[0]]]
        res_counter = [Counter(e) for e in res]

        for i in range(1, len_nums):
            sub_re = []
            for e in res:
                temp_e = e.copy()
                temp_e.append(nums[i])
                sub_re.append(temp_e.copy())

            for sub_re_e in sub_re:
                sub_re_e_counter = Counter(sub_re_e)
                if sub_re_e_counter not in res_counter:
                    res_counter.append(sub_re_e_counter)
                    res.append(sub_re_e)

        return res

from copy import copy
class Solution1:
    def subsetsWithDup(self, nums):
        nums.sort()
        len_nums = len(nums)
        return self._subset(nums, len_nums, 0, [[]])

    def _subset(self, nums, len_nums, start, sub_re):
        if start == len_nums:
            return sub_re

        for i in range(start, len_nums):
            temp = []
            for e in sub_re:
                new_e = copy(e)
                new_e.append(nums[i])
                temp.append(new_e)

            for temp_e in temp:
                if temp_e not in sub_re:
                    sub_re.append(temp_e)
            sub_re = self._subset(nums, len_nums, i+1, sub_re)
            return sub_re

class Solution3:
    def __init__(self):
        self.res = []
    def subsetsWithDup(self, nums):
        sort_nums = sorted(nums)
        self._sub_set(sort_nums, 0, [])
        return self.res

    def _sub_set(self, nums, start_i, re):
        self.res.append(re)

        while start_i < len(nums):
            e = nums[start_i]
            re1 = copy(re)
            re1.append(e)
            self._sub_set(nums, start_i+1, re1)

            while start_i+1 < len(nums) and nums[start_i+1] == e:
                start_i += 1
            start_i += 1

        return


if __name__ == "__main__":
    so = Solution3()
    nums = [1,1]
    re = so.subsetsWithDup(nums)
    print(re)