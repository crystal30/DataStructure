from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = Counter(nums1)
        res = []
        for num2 in nums2:
            if num2 in dict1:
                res.append(num2)
                if dict1[num2] == 1:
                    dict1.pop(num2)
                else:
                    dict1[num2] -= 1
        return res
if __name__ == '__main__':

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    so = Solution()
    print(so.intersect(nums1, nums2))