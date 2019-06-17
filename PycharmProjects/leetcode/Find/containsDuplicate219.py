class Solution:
    #暴力破解：time limited out
    #时间复杂度：O(N*K),N = len(nums), K = k
    #空间复杂度：O(1)
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            j = i+1
            while j < n and j-i <= k:
                if nums[i] == nums[j]:
                    return True
                j += 1
        return False

    #滑动窗口
    #时间复杂度：?
    def containsNearbyDuplicate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0 or k == 0:
            return False
        l = 0
        r = 1
        while l < n:
            while r < n and r - l <= k:
                #时间复杂度：O(k)?
                if nums[r] in nums[l:r]:
                    return True
                r += 1
            l += 1
        return False

    # frozenset, set #注意：不能使用frozenset，因为其没有add和remove功能
    # 滑动窗口 + 查找表
    #56ms
    #时间复杂度：O(n)#如果set的添加和删除操作的时间复杂度是O(1)的话
    #空间复杂度：O(k)
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in record:
                return True
            record.add(nums[i])

            if (len(record) == k+1):
                record.remove(nums[i-k])
        return False

    # frozenset, set
    # 滑动窗口 + 查找表
    # 这次用list代替set
    #time limited out
    #为什么list没有set快呢，set用的是哈希？那frozenset 用的是什么呢？
    def containsNearbyDuplicate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        record = list()
        n = len(nums)
        for i in range(n):
            if nums[i] in record:
                return True
            record.append(nums[i])

            if (len(record) == k+1):
                record.remove(nums[i-k])
        return False




if __name__ == "__main__":
    nums = [0, 1, 2, 3, 2, 5]
    k = 3
    so = Solution()
    re = so.containsNearbyDuplicate2(nums, k)
    pass

