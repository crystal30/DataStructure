# -*-coding: utf-8 -*-
import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return heapq.nlargest(k, nums)[-1]



if __name__ == "__main__":
    so = Solution()
    nums =  [3,2,3,1,2,4,5,5,6]
    k = 4
    so.findKthLargest(nums, k)




