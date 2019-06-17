class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)



if __name__ == '__main__':

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    so = Solution()
    print(so.intersection(nums1, nums2))



