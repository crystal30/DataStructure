class Solution:
    def intersection(self, nums1, nums2):

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        re = []
        if len(set_nums1) <= len(set_nums2):
            for e in set_nums1:
                if e in set_nums2:
                    re.append(e)
        else:
            for e in set_nums2:
                if e in set_nums1:
                    re.append(e)

        return re

if __name__ == "__main__":
    so = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    re = so.intersection(nums1, nums2)
    print(re)


