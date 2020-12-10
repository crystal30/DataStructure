from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):

        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
        re_dict = dict()
        if len(nums1_dict) <= len(nums2_dict):
            for k in nums1_dict.keys():
                if k in nums2_dict.keys():
                    re_dict[k] = min(nums1_dict[k], nums2_dict[k])
        else:
            for k in nums2_dict.keys():
                if k in nums1_dict.keys():
                    re_dict[k] = min(nums1_dict[k], nums2_dict[k])

        re = []
        for k in re_dict.keys():
            for _ in range(re_dict[k]):
               re.append(k)

        return re

if __name__ == "__main__":
    so = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    re = so.intersect(nums1, nums2)
    print(re)
