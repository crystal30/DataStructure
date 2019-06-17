class Solution(object):
    #若list的sum操作也为O(n)的话则时间复杂度O(n3)
    #time Limit Exceeded
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len([x for x in nums if x>=s])>0:
            return 1
        #当nums中不存在>=s的元素时，若存在一个解法，则 len(nums)>=len(subArray) >= 2
        res = len(nums) + 1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j+1]) >= s and res > j+1-i:
                    res = j+1-i

        if res == len(nums)+1:
            return 0
        else:
            return res

    #Time limit out，说指针遍历
    #对sum(nums[i:j])改进
    #若list中的sum()操作为O(n)的话，时间复杂度为O(n2)
    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i,j,res = 0, 1, len(nums)+1
        #nums[i,j)为符合条件的子序列，该子序列的长度为j-i,res为最终的返回值
        #注意，list中的nums[i,j]是前闭后开的，是不包括元素nums[j]的
        while j<=len(nums):
            if sum(nums[i:j])<s:
                j += 1
            else:# sum(nums[i,j]) >=s:
                if j-i < res:
                    res = j-i
                i += 1
            if i==j:
                break
        return 0 if res == len(nums)+1 else res

    #28 ms,双指针遍历，滑动窗口，对sum操作进行优化
    #注意考虑空数组的情况
    #时间复杂度O(n)
    def minSubArrayLen3(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #空数组的情况
        if n == 0:
            return 0
        #非空数组的情况
        i,j,res = 0, 0, n+1
        #nums[i,j]为符合条件的子序列，该子序列的长度为j-i,res为最终的返回值
        #注意，list中的nums[i,j]是前闭后开的，是不包括元素nums[j]的
        nums_sum = nums[0]
        while True:
            if nums_sum < s:
                j += 1
                if j == n:
                    break
                nums_sum += nums[j]
            else: # nums_sum >=s:
                if j == i:
                    return 1
                elif j+1-i<res:
                    res = j+1-i
                nums_sum -= nums[i]
                i += 1

        return 0 if res == n+1 else res
    #good
    #虽然minSubArrayLen3 的另一种写法，这种写法更推荐
    #28 ms
    def minSubArrayLen3_1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        #定义nums[i,j]为滑动窗口，找出sum(nums[i,j])>=s 的子数组，不断的更新，最终输出最小长度
        i = 0
        j = -1
        n = len(nums)
        res = n + 1
        sums = 0
        while i < n:
            if j+1 < n and s > sums:
                sums += nums[j+1]
                j += 1
            else: # j+1 >= n or s <= sums
                sums -= nums[i]
                i += 1

            if s <= sums:
                res = min(res, j + 1 - i)

        return 0 if res == n+1 else res

    #数组依次存放和，用 两个指针遍历
    #28 ms
    #时间复杂度O(n)
    #空间复杂度O（1）
    def minSubArrayLen4(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        #将nums[i] 中的元素变为前i个元素的和
        for i in range(1,n):
            nums[i] = nums[i-1] + nums[i]
        nums.insert(0,0)

        i,j, res = 0, 1, n+1
        while j <= n:
            if nums[j] - nums[i] < s:
                j += 1
            else:
                res = min(res, j - i)
                if res == 1:
                    return res
                i += 1
        return 0 if res == n+1 else res

if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    s = 7
    so = Solution()
    i = so.minSubArrayLen3_1(s, nums)
    pass