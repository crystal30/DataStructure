# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

class Solution(object):
    #时间复杂度，m*n,
    #28ms
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #对特殊情况进行考虑
        if m==0:
            nums1[:] = nums2
            return
        if n == 0:
            return
        i = 0 #i,j分别表示nums1,和nums2的下标
        j = 0
        while i < m:
            if nums1[i] <= nums2[j]:
                i += 1
            else: #nums1[i] > nums2[j]
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i += 1
                # 将nums2[j] 放到合适的位置
                t = j #t存放nums2[j]应该放的位置
                while t < n:
                    if t+1<n and nums2[t] > nums2[t+1]:
                        nums2[t], nums2[t+1] = nums2[t+1], nums2[t]
                        t += 1
                    else:#nums2[t] <= nums2[t+1]
                        break
        nums1[i:] = nums2[j:]

if __name__ == "__main__":
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    so = Solution()
    so.merge(nums1, m, nums2, n)
    pass