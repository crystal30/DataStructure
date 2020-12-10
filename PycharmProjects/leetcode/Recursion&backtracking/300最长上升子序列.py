from copy import copy


class Solution:
    def __init__(self):
        self.max_length = 0
        self.visited = None
    def lengthOfLIS(self, nums):
        len_nums = len(nums)
        self.visited = [False] * len_nums
        self._length_of_lts(nums, 0, 0, 0)
        return self.max_length

    def _length_of_lts(self, nums, start_i, p_e, len_sub_nums):
        if len_sub_nums > self.max_length:
            self.max_length = len_sub_nums

        while start_i < len(nums):
            e = nums[start_i]
            if len_sub_nums > 0:
                if e <= p_e:
                    start_i += 1
                    continue
            self.visited[start_i] = True
            self._length_of_lts(nums,  start_i+1, e, len_sub_nums+1)

            while len_sub_nums == 0 and start_i+1 < len(nums) and self.visited[start_i+1] is True:
                start_i += 1
            start_i += 1

        return



class Solution:
    def __init__(self):
        self.visited = None
    def lengthOfLIS(self, nums):
        self.visited = [0] * len(nums)
        max_length = 0
        for i in range(len(nums)):
            re = self._length_of_lts(nums, i)
            if re > max_length:
                max_length = re
        return max_length

    def _length_of_lts(self, nums, start_i):
        if self.visited[start_i] != 0:
            return self.visited[start_i]

        e = nums[start_i]
        if start_i == len(nums)-1 or e >= max(nums[start_i+1:]):
            self.visited[start_i] = 1
            return 1


        re_list = []
        for i in range(start_i+1, len(nums)):
            if nums[i] > e:
                re = self._length_of_lts(nums, i)
                re_list.append(re)
        start_i_max_length = 1 + max(re_list)
        self.visited[start_i] = start_i_max_length
        return start_i_max_length




if __name__ == "__main__":
    so = Solution()
    nums = [1,1,1,1,1]
    re = so.lengthOfLIS(nums)
    print(re)