#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [2,0,2,1,1,0]
from random import randint
class Solution:
    #算法的整体复杂度为O（n）+ O(nlogn)+O(n) ~ O(nlogn)
    #84 ms
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #起初的理解，其就是一个排序，在这里选用堆排序
        #构成一个最小堆，时间复杂度O(n)
        self.minheap(nums)
        n = len(nums)-1
        #下边的过程类似于最小堆堆排序，不过排出来是从大到小的,时间复杂度O(nlogn)
        while n > 0:
            nums[0], nums[n] = nums[n], nums[0]
            n -= 1
            self.shiftDown(0, nums, n)

        #nums.reverse 的时间复杂度？没看源码，应该是O(n)的
        nums.reverse()

    def minheap(self, nums):
        n = len(nums)-1
        for i in range((n-1)//2,-1,-1):
            self.shiftDown(i, nums, n)

    def shiftDown(self, i, nums, n):
        '''
        :param i: 对nums[i]进行下沉操作，把其放到合适的位置
        :param nums:
        :param n:  list的下标是从0开始的，n表示的是最后一个元素的下标
        :return:
        '''
        j = i*2+1 #j中最终存放的是i的左孩子和右孩子中最小的那个元素的下标，这里初始化为左孩子
        while j <= n:
            if j+1 <= n and nums[j] > nums[j+1]:
                j += 1
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                i = j
                j = i *2 + 1
            else:
                break

    #改进1，形成最小堆后，排序之后直接就是从小到大的
    #此时算法的复杂度是O(n) + O(nlogn) ~O（nlogn）
    #40 ms
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #起初的理解，其就是一个排序，在这里选用堆排序
        #构成一个最小堆，时间复杂度O(n)
        self.minheap1(nums)
        n = len(nums)-1
        #下边的过程类似于最小堆堆排序，不过排出来是从大到小的,时间复杂度O(nlogn)
        while n > 0:
            nums[0], nums[n] = nums[n], nums[0]
            n -= 1
            self.shiftDown1(0, nums, n)

    #将数组构成最大堆
    def minheap1(self, nums):
        n = len(nums)-1
        for i in range((n-1)//2,-1,-1):
            self.shiftDown1(i, nums, n)
    #构成最大堆的shiftDown
    def shiftDown1(self, i, nums, n):
        '''
        :param i: 对nums[i]进行下沉操作，把其放到合适的位置
        :param nums:
        :param n:  list的下标是从0开始的，n表示的是最后一个元素的下标
        :return:
        '''
        j = i*2+1 #j中最终存放的是i的左孩子和右孩子中最大的那个元素的下标，这里初始化为左孩子
        while j <= n:
            if j+1 <= n and nums[j] < nums[j+1]:
                j += 1
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                i = j
                j = i *2 + 1
            else:
                break
    #考虑特殊情况1：当是空数组时，minheap中for循环不执行，sortColors中的while循环也不执行，即什么也不做
    #考虑特殊情况2：当数组中只有一种元素时，即所有元素都相等，minheap 进入for循环，执行shiftDown，经条件判断什么也不做
                # 在sortColors的while循环中，每次交换相等的元素，对程序也没有什么影响，当然在这里也可以加一个判断
                #当nums[0] == nums[n]时...  当nums[0] != nums[n]时....
    #其实感觉核心就是排序，其它排序方法应该也可以
    #是不是用3路快排会更好一点，因为这里　只有0，1，2这3个不同的元素。

    #改进2：
    #使用3路快速排序
    #24 ms 快排时间复杂度O(nlogn)，但由于含有大量的重复元素，所以复杂度肯定小于O(nlogn)
    #怀疑：三路快排的时间复杂度到底是多少？
    def sortColors2(self, nums):
        n = len(nums)
        t = randint(0,n-1)
        nums[0], nums[t] = nums[t], nums[0]
        #3路快速排序
        #假设l表示最左侧的元素，nums[l]为目标元素；[l+1,lt]中为<v的元素，[gt,r]中为>v的元素，
        # [lt+1, i-1]中存放的为==v的元素，nums[i]表示正要检测的元素
        self.quicksort3(0,n-1,nums)

    #需要排序的数组为nums，排序范围为[l,r],前闭后闭的区间
    def quicksort3(self, l, r, nums):
        if l >= r:
            return
        lt, gt, i = l, r + 1, l + 1
        while i < gt:
            if nums[i] > nums[l]:
                gt -= 1
                nums[i], nums[gt] = nums[gt], nums[i]
            elif nums[i] < nums[l]:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            else:  # nums[i]==nums[l]
                i += 1
        nums[l], nums[lt] = nums[lt], nums[l]
        self.quicksort3(0, lt - 1, nums)
        self.quicksort3(gt, r, nums)


    #利用三路快排的思路使程序更简单
    #根据题目，只有0，1，2这三种元素，所以令nums[l,lt]中存放小于1的元素(即0)，
    # 令nums[lt+1,i-1]中存放等于1的元素，令[gt,r]中存放大于1的元素，即2
    #时间复杂度为O(n),因为只要遍历一遍数组，就可以将0，1，2放到合适的位置
    #24ms
    @classmethod
    def sortColors3(cls, nums):
        lt = -1
        gt = len(nums)
        i = 0
        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1


    #改进4：
    #记数排序的思路
    #用一个数组count来记录0，1，2的频次
    #时间复杂度O（n）
    #空间复杂度 O（k），这里k=3（因为有3个不同的元素）
    # 32 ms
    def sortColors4(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in nums:
            count[i] += 1
        index = 0
        for _ in range(count[0]):
            nums[index] = 0
            index += 1
        for _ in range(count[1]):
            nums[index] = 1
            index += 1
        for _ in range(count[2]):
            nums[index] = 2
            index += 1

    #对sortColors4的改进
    #28ms
    def sortColors5(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for i in nums:
            count[i] += 1
        index = 0
        for i in range(len(count)):
            for _ in range(count[i]):
                nums[index] = i
                index += 1

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    so = Solution()
    so.sortColors5(nums)
    pass
