# -*- coding: utf-8 -*-
class Solution:
    def twoSum(self, nums, target: int):

        n = len(nums)

        for i in range(n):
            find_e = target - nums[i]
            index = self.binarySearch(nums[i+1 : n], find_e)
            if index != -1:
                return [i, index + i + 1]



    def binarySearch(self, sub_nums, find_e):
        # 搜寻nums_sort[l,r]间是否存在 find_e, 若存在，返回True， 若不存在，返回False
        sub_nums_sort = sorted(sub_nums)
        l = 0
        r = len(sub_nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if sub_nums_sort[mid] > find_e:
                r = mid - 1
            elif sub_nums_sort[mid] < find_e:
                l = mid + 1
            else:
                return sub_nums.index(find_e)

        return -1

    # 利用查找表的方式实现
    def twoSum1(self, nums, target: int):
        nums_dict = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = [i]
            else:
                nums_dict[nums[i]].append(i)
        for i in range(n):
            find_e = target - nums[i]
            if find_e in nums_dict.keys():
                find_e_indexs = nums_dict[find_e]
                if len(find_e_indexs) >= 2:
                    for op_i in find_e_indexs:
                        if op_i != i:
                            return [i, op_i]
                else:
                    if nums_dict[find_e] != [i]:
                        return [i] + nums_dict[find_e]

    # 由于数组中两个位置的值可能是一样的，故只将v前面的元素放入查找表中
    # 感觉这种方法不太好想
    def twoSum2(self, nums, target):
        n = len(nums)
        nums_dict = dict()
        nums_dict[nums[0]] = 0
        for i in range(1, n):
            find_e = target - nums[i]
            if find_e in nums_dict:
                return [nums_dict[find_e], i]
            else:
                nums_dict[nums[i]] = i




if __name__ == "__main__":
    so = Solution()
    nums = [7,2,2,11,15]
    target = 9
    re = so.twoSum1(nums, target)
    print(re)
