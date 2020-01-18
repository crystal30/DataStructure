from random import randint
class Solution(object):

    #Time Limit Exceeded
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    #假设nums[0]为标定元素， nums[1:gt]中的元素>v, nums[gt+1,i-1]中的元素 ==v，nums[lt:]<v
        l = 0
        r = len(nums)-1
        while True:
            gt, i, lt = l, l + 1, r + 1
            v = nums[l]
            while i<lt:
                if nums[i] > v:
                    nums[gt+1], nums[i] = nums[i], nums[gt+1]
                    gt += 1
                    i += 1
                elif nums[i] < v:
                    nums[lt-1], nums[i] = nums[i], nums[lt-1]
                    lt -= 1
                else:#nums[i] == v
                    i += 1
            nums[l], nums[gt] = nums[gt], nums[l]
            #nums[l]的位置即在gt
            if gt>k-1:
                l = 0
                r = gt - 1
            elif gt<=k-1 and lt>k-1:
                return nums[gt]
            elif lt <= k-1:
                l = lt
                r = len(nums)-1

    # 268ms ,时间复杂度较高
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 假设nums[0]为标定元素， nums[1:gt]中的元素>v, nums[gt+1,i-1]中的元素 ==v，nums[lt:]<v
        l = 0
        r = len(nums) - 1
        #每次丢弃一半的数据，n个数据除以多少次2，最后等于0？logn，
        # 故最外层的时间复杂度为O(logn),最差情况下是O(n)
        #所以总的时间复杂度是Onlogn
        #还有一种计算复杂度的想法，复杂度为n + 1/2n + 1/4n + 1/8n + ...+2，这个目前不知道该怎么算
        #一种算法：正着算，a1 = n, q= 1/2, an = 2
        #另一种算法，逆着算，a1 = 2,q = 2, an = n
        #感觉两种算出来的不一样
        #通过实验的比较，感觉算法的时间复杂度忽好，忽坏，判断不了
        #但是视频中说可以利用 快排的思想，写出O(n)的程序
        while True:
            tt = randint(l, r)
            nums[l], nums[tt] = nums[tt], nums[l]
            gt, i, lt = l, l + 1, r + 1
            v = nums[l]
            #对每个元素都要遍历一遍，将nums[l],放到合适的位置，这里我们认为每次的数据量将减少一半
            while i < lt:
                if nums[i] > v:
                    nums[gt + 1], nums[i] = nums[i], nums[gt + 1]
                    gt += 1
                    i += 1
                elif nums[i] < v:
                    nums[lt - 1], nums[i] = nums[i], nums[lt - 1]
                    lt -= 1
                else:  # nums[i] == v
                    i += 1
            nums[l], nums[gt] = nums[gt], nums[l]
            # nums[l]的位置即在gt
            if gt > k - 1:
                l = 0
                r = gt - 1
            elif gt <= k - 1 and lt > k - 1:
                return nums[gt]
            elif lt <= k - 1:
                l = lt
                r = len(nums) - 1

    #时间复杂度偏高，有没有什么更好的思路？

    # 自己写的，一次性通过，但是时间复杂度较高
    def findKthLargest3(self, nums, k):
        n = len(nums)
        for i in range(k):
            max_index = self._insertSort(i, n, nums)
            nums[i], nums[max_index] = nums[max_index], nums[i]
        return nums[k-1]

    def _insertSort(self, i, n, nums):
        '''

        :param i: 搜索 nums[i:]的最大的元素
        :param n: nums 数组总的长度
        :param nums:
        :return:
        '''
        temp = nums[i]
        max_index = i
        for j in range(i+1 , n):
            if nums[j] > temp:
                temp = nums[j]
                max_index = j

        return max_index

    def findKthLargest4(self, nums, k):
        n = len(nums)
        if n >= 1:
            r = lt = n
            l = gt = 0
            while lt >= gt:
                if lt == k-1:
                    return nums[k-1]

                if lt >= k:
                    r = lt
                    lt = self.__quickSort(nums, l, lt)
                else:
                    # if lt == 0:
                    #     gt += 1
                    l = lt+1
                    lt = self.__quickSort(nums, lt+1, r)

            return nums[k-1]

    def __quickSort(self, nums, l, r):
        # 对nums[l:r)进行快速排序
        gt = l # nums(0, gt] >= nums[0], nums[lt:]<nums[0]
        lt = r
        temp = nums[l]
        i = l+1
        while i < lt:
            if nums[i] > temp:
                i += 1
                gt += 1
            else:
                lt -= 1
                nums[i], nums[lt] = nums[lt], nums[i]
        nums[i - 1], nums[l] = nums[l], nums[i - 1]
        return i-1


from TestTime import TestTime
from time import time

if __name__ == "__main__":
    nums = [3, 1, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    k = 21
    so = Solution()
    re = so.findKthLargest4(nums, k)
    pass








