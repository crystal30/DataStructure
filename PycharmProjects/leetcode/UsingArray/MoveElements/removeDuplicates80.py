#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [1,1,1,2,2,3]
class Solution:
    #52 ms
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #考虑特注情况：空数组，
        if nums == []:
            return 0
        #考虑特殊情况：全部是重复元素的数组，此时是遍历一遍数组，


        j = 0 #[:j]中存放的为我们需要的元素
        count = 1 #记录重复元素的个数，初始的为1，但是不能超过2
        for i in range(1,len(nums)):
            if nums[i] == nums[j] and count < 2:
                j += 1
                nums[j] = nums[i]
                count += 1
            # 考虑特殊情况：没有重复元素的数组，每次都进入下边的语句，即每次都自己给自己赋值
            elif nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                count = 1
        return j + 1

    #改进，对特殊情况3加一个条件判断语句
    # 88ms，判断语句似乎更消耗时间
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #考虑特注情况1：空数组，
        if nums == []:
            return 0
        #考虑特殊情况2：全部是重复元素的数组，此时是遍历一遍数组，

        j = 0 #[:j]中存放的为我们需要的元素
        count = 1 #记录重复元素的个数，初始的为1，但是不能超过2
        for i in range(1,len(nums)):
            if nums[i] == nums[j] and count < 2:
                j += 1
                nums[j] = nums[i]
                count += 1
            # 考虑特殊情况3：没有重复元素的数组，每次都进入下边的语句，即每次都自己给自己赋值，
            #此时添加一个判断语句
            elif nums[i] != nums[j]:
                j += 1
                if i != j:
                    nums[j] = nums[i]
                count = 1
        return j + 1


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    so = Solution()
    re = so.removeDuplicates(nums)
    print(re)
    pass



