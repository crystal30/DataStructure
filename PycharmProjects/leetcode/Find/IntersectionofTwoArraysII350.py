from  collections import Counter
class Solution:
    #44 ms
    #总体的时间复杂度是O(max(len(nums1),len(nums2))
    #空间复杂度O(n)
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #不太清楚Counter的时间复杂度，没有看过源码
        #在这里，认为是O(len(nums1))
        dd_1 = Counter(nums1)
        #O(len(nums2)
        dd_2 = Counter(nums2)
        res = []
        #python 中set和map都是以哈希的形式实现的，所以查找，删除，添加元素的时间复杂度为O(1)
        #O（len(dd_1)）
        for k in dd_1:
            if k in dd_2:
                # res += [k]*min(dd_1[k], dd_2[k])
                res.extend([k] * min(dd_1[k], dd_2[k])) #用这句话的效率更高一点
        return res

    #48 ms
    #时间复杂度：O(max(len(nums1), len(nums2))
    #空间复杂度：O（n）
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dd_1 = Counter(nums1)
        res = []
        for k in nums2:
            if k in dd_1 and dd_1[k] != 0:
                res.append(k)
                dd_1[k] -= 1
        return res


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2,2]
    so = Solution()
    re = so.intersect1(nums1,nums2)
    pass



