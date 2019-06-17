class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        set1 = set(nums1)
        # set1 = set()
        # for num1 in nums1:
        #     set1.add(num1)

        res = []
        for num2 in nums2:
            if num2 in set1:
                res.append(num2)
                set1.remove(num2)
        return res

if __name__ == '__main__':

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    so = Solution()
    print(so.intersection(nums1, nums2))



