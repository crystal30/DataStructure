class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0 #存放不是数组中不是val的元素的第一个下标，
              # 即最终[0,j)中存放的元素值不为val，
        for i in range(len(nums)):
            if nums[i]  != val:
                if j != i:
                    nums[j] = nums[i]
                j += 1
        #此时nums[j:]中还是原始nums[j:]，但是题目中未对这些做要求，所以可不语考虑
        return j