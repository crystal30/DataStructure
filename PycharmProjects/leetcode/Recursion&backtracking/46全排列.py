class Solution:
    def __init__(self):
        self.re = []

    def permute(self, nums):
        self.sub_permute(nums, 0, [])
        return self.re

    def sub_permute(self, nums, index, sub_re):

        len_nums = len(nums)
        if index == len_nums:
            if sub_re != []:
                self.re.append(sub_re)
            return

        temp = sub_re.copy()
        temp.append(nums[index])

        sub_nums = nums.copy()
        sub_nums.pop(index)

        self.sub_permute(sub_nums, 0, temp)

        if index + 1 < len_nums:
            self.sub_permute(nums, index+1, sub_re)
        return

from copy import copy
class Solution1:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        len_nums = len(nums)
        nums_visited = [False] * len_nums
        self._pernute(nums, len_nums, [], nums_visited)
        return self.res

    def _pernute(self, nums, len_nums, sub_list, nums_visited):
        if len(sub_list) == len_nums:
            self.res.append(copy(sub_list))
            return

        for i in range(len_nums):
            if nums_visited[i] == False:
                sub_list.append(nums[i])
                nums_visited[i] = True
                self._pernute(nums, len_nums, sub_list, nums_visited)
                sub_list.pop()
                nums_visited[i] = False

        return

if __name__ == "__main__":
    so = Solution1()
    nums = [2,4,6]
    re = so.permute(nums)
    print(re)
