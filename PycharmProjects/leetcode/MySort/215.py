class Solution:
    def findKthLargest(self, nums, k):
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


if __name__ == "__main__":

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    so = Solution()
    re = so.findKthLargest(nums, k)
    pass




