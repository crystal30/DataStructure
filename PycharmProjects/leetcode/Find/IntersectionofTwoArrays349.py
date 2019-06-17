class Solution:
    #60ms
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(set(nums2)))
    #80ms
    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [_ for _ in nums1 if _ in nums2]

    #72ms
    #时间复杂度O(len(nums1))
    #空间复杂度：O(len(nums1))
    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [_ for _ in set(nums1) if _ in nums2]

