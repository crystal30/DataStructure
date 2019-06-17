#!/usr/bin/env python3
# -*- coding utf-8 -*-
from random import randint
class Solution:
    # time limited exceed
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        #用我们自己写的普通快排不行，三路快排的时间符合要求，但是仍没有库中的sort函数快
        self.selectionSort3(nums, 0, len(nums)-1)
        # nums.sort()
        result = []
        for i,a in enumerate(nums):
            if i >= 1 and nums[i-1]==a:
                continue
            j = i + 1
            k = n-1
            while j<k:
                if a + nums[j] + nums[k] < 0:
                    j += 1
                elif a + nums[j] + nums[k] > 0:
                    k -= 1
                else: #a + nums[j] + nums[k] == target
                    result.append([nums[i], nums[j], nums[k]])
                    while j+1 <k and nums[j+1] == nums[j]:
                        j += 1
                    while j + 1 < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return result

    #选择排序，最基本的写法
    def selectionSort(self, nums, l, r):
        if l >= r:
            return None

        random_num = randint(l+1,r)
        nums[l], nums[random_num] = nums[random_num], nums[l]
        v = nums[l]
        i = l+1 #i为当前元素的下标
        j = l #nums[:j]中存放的为 <v 的元素，nums[j+1:i-1]>v
        while i <= r:
            if j+1 <= r and nums[i] < v:
                nums[i], nums[j+1] = nums[j+1], nums[i]
                i += 1
                j += 1
            else:# j+1 >= n or nums[i] >=v
                i += 1
        nums[l], nums[j] = nums[j], nums[l]
        self.selectionSort(nums, l, j-1)
        self.selectionSort(nums, j+1, r)

    #三路快排,排序范围是在nums[l,r]闭区间
    def selectionSort3(self, nums, l, r):
        if l >= r:
            return None
        random_num = randint(l + 1, r)
        nums[l], nums[random_num] = nums[random_num], nums[l]
        i, j, k = l + 1, l, r + 1
        v = nums[l]
        while i < k:
            if j <= r and nums[i] < v:
                nums[j + 1], nums[i] = nums[i], nums[j + 1]
                i += 1
                j += 1
            elif k - 1 > l and nums[i] > v:
                nums[i], nums[k - 1] = nums[k - 1], nums[i]
                k -= 1
            else:  # nums[i] == v
                i += 1
        nums[l], nums[j] = nums[j], nums[l]
        self.selectionSort3(nums, l, j - 1)
        self.selectionSort3(nums, k, r)

    #time limited out,即使是用库中的排序函数
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        self.selectionSort(nums, 0, n-1)
        # nums.sort()
        result = []
        for i in range(n):
            target = 0 - nums[i]
            for j in range(i+1, n):
                complement = target - nums[j]
                if self.binarySearch(nums[j+1:], complement) != None \
                        and [nums[i], nums[j], complement] not in result:
                    result.append([nums[i], nums[j], complement])
        return result


    def binarySearch(self, nums, e):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > e:
                r = mid-1
            elif nums[mid] < e:
                l = mid+1
            else:
                return e
        return None

    #good
    #696ms
    #时间复杂度：O(n2)
    #空间复杂度：O（len(result)）
    #思路：a = nums[i], b = nums[j], c = nums[k],
    # 先固定住a，然后采用对撞指针的方式找出nums[j],nums[k]
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        # self.selectionSort(nums, 0, len(nums)-1)
        nums.sort()
        result = []
        for i in range(n-2):
            if i >= 1 and nums[i - 1] == nums[i]:
                continue
            if nums[i] <= 0:
                j = i + 1
                k = n - 1
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total < 0:
                        j += 1
                    elif total > 0:
                        k -= 1
                    else:  # a + nums[j] + nums[k] == target
                        result.append([nums[i], nums[j], nums[k]])
                        while j + 1 < k and nums[j + 1] == nums[j]:
                            j += 1
                        while j + 1 < k and nums[k - 1] == nums[k]:
                            k -= 1
                        j += 1
                        k -= 1
        return result

if __name__ == "__main__":
    # nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    #[[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
    nums = [-1, 0, 1, 2, -1, -4]
    so = Solution()
    re = so.threeSum(nums)
    pass


    # [
    #     [-1, 0, 1],
    #     [-1, -1, 2]
    # ]