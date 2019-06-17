from random import randint
class Solution:
    #暴力破解
    #时间复杂度：O(n2),肯定超时
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return i,j

    #用选择排序对数组进行排序
    #对撞指针
    #96ms
    #总体时间复杂度O(nlogn)
    def twoSum1(self, nums, target):
        n = len(nums)
        index = [_ for _ in range(n)]
        l = 0
        r = n-1
        #时间复杂度 O(nlogn)
        self.indexSelectionSort(nums, index, l, r)
        #对撞指针
        i = 0
        j = len(nums)-1
        #时间复杂度O(n)
        while True:
            if nums[index[i]] + nums[index[j]] < target:
                i += 1
            elif nums[index[i]] + nums[index[j]] > target:
                j -= 1
            else:
                return index[i], index[j]

    #时间复杂度O(nlogn)
    def indexSelectionSort(self, nums, index, l, r):
        #nums[1:j]<v, nums[j+1:i-1]>v
        if r<=l:
            return
        t = randint(l,r)
        index[l], index[t] = index[t], index[l]
        i = l + 1
        j = l
        v = nums[index[l]]
        while i <= r:
            if j+1 <= r and nums[index[i]]<v:
                index[j+1], index[i] = index[i], index[j+1]
                j += 1
                i += 1
            else:
                i += 1
        index[l], index[j] = index[j], index[l]
        self.indexSelectionSort(nums, index, l, j-1)
        self.indexSelectionSort(nums, index, j+1, r)

    #40 ms
    #时间复杂度：O(n), 空间复杂度：O(n)
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #利用查找表
        record = {}
        for i in range(len(nums)):
            if nums[i] not in record:
                record[nums[i]] = i
            t = target - nums[i]
            if t in record and record[t] != i:
                return [record[t],i]

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    so = Solution()
    re = so.twoSum2(nums, target)
    pass


