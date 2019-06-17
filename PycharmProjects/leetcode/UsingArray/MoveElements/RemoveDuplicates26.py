#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    #错误的示范
    #nums = list(set(nums))中，第一个nums与第二个nums所指的对象是不一样的，即id不一样，
    # 所以，加入我们传入的nums为[1,1,2]时，第一个nums为[1,2],reurn len(nums) = 2
    # 但第二个nums仍指向[1,1,2]（即后台数据nums）
    #故当执行此程序时，leetcode报错：Input:[1,1,2] Output:[1,1] Expected:[1,2]
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        return len(nums)

    #超出时间限制
    #该算法的复杂度通过实验证明为O(n2)级别的，
    # 理论分析时间复杂度：
    # 首先一层while循环是O(n),pop(i)有可能是O(n)级别的，
    # 即使pop(i)的复杂度不是O(n)级别的，if nums[i] in nums[:i]，这个判断语句也是O(n)级别的
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 1
        j = 1 #检测的数组中元素的个数
        while j < n:
            if nums[i] in nums[:i]:
                nums.pop(i)
            else:
                i += 1
            j += 1
        return len(nums)

    #改进，注意，数组是有序的
    #时间复杂度为O（n），此时只要遍历一遍数组即可
    #注意考虑一下数组为空，或是数组没有重复元素的情况,
    #64ms
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0 #假设nums[:j）存放的是没有重复的元素,j表示存放不重复元素的第一个下标
        #考虑空数组的情况
        if nums == []:
            return 0

        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

    #改进3，再次考虑极端的情况
    #考虑一下数组为空，或是数组没有重复元素的情况，或是数组中全部是重复元素
    #72ms
    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0 #假设nums[:j）存放的是没有重复的元素,j表示存放不重复元素的第一个下标
        if nums == []:
            return 0

        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                if i != j: #考虑数组中全部是重复元素时
                    nums[j] = nums[i]

        return j+1

    #更多的思考，如果数组不是有序的呢，本道题目的解题方法就不合适了。
    #idea：将数组形成最小堆（用heapify），其时间复杂度是O(n),每次从堆中取出一个元素，
    # 若下一个元素与上一个元素不等，将其放入数组的最后边（但注意：最小堆中并不包含此元素）
    # 若下一个元素与上一个元素相等，将其舍弃，
    #将最小堆中的元素全部抛完时，数组中剩下的就是不重复的元素，时间复杂度是O(nlogn)
    #由于形成最小堆和后边的依次抛元素是串行的，故总的时间复杂度是(O(nlogn) + O(n))~O(nlogn)



if __name__ == "__main__":
    # arr = [1,1,2]
    arr = []
    so = Solution()
    re = so.removeDuplicates2(arr)
    print(re)
