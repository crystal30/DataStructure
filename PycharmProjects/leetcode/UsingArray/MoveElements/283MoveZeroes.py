#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# [0,1,0,3,12]
# [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = 0 #表示检测的数字的个数
        i = 0 #表示正在检测的元素的下标
        while n < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            n += 1

    #运行时间：60ms
    #思路：将非0的元素依次填入到数组nums[0,j)，最后，再将nums[j：]置0
    def moveZeroes1(self, nums):
        j = 0 #存放下一个不是0的元素的下标，即[0,j)中存放的是非0 元素，j<len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        #当所有的元素都遍历过一遍了，即将所有非0的元素取出依次放在nums[0,j)中，剩下的位置只用补0即可。
        nums[j:]=[0]*(len(nums)-j)

    #moveZeroes1改进，把所有元素都遍历一遍之后，即能将非0元素依次放入nums[0,j)，又可以将数组nums[j:]全部置0呢
    #运行时间48ms
    def moveZeroes2(self, nums):
        j = 0  # 存放下一个不是0的元素的下标，即[0,j)中存放的是非0 元素，j<len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

    #思考一些极端的情况，
    #1。该数组中如果全部为0，进入for循环，判断一遍什么也不做
    #2。该数组中若全部为非0元素，进入for循环，j始终等于i，即数组中的元素全部都自己跟自己交换了一遍
    #这个可以避免吗？
    #虽然少了交换，但是多了条件判断，可能测试用例中这种极端的例子（全是非0元素的数组）比较少，
    # 所以最终运行的时间是56ms
    #同样的思路，不同的语言出来的时间效果也可能不同
    def moveZeroes3(self, nums):
        j = 0  # 存放下一个不是0的元素的下标，即[0,j)中存放的是非0 元素，j<len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    so = Solution()
    so.moveZeroes3(nums)
    print(nums)


