from collections import Counter
class Solution:
    #滑动窗口+查找表set
    #时间复杂度为O(n)
    #48ms
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)
        return False

    #利用查找表map
    #时间复杂度：O(n)
    #52ms
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dd = Counter(nums) #时间复杂度认为是O(n)
        if len(dd)>0 and max(dd.values()) > 1:
            return True
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    so = Solution()
    so.containsDuplicate(nums)
