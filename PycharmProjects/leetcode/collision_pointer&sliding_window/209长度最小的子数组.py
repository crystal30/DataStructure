class Solution:
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            if nums[0] < s:
                return 0
            else:
                return 1

        if sum(nums) < s:
            return 0

        i = 0
        j = 1
        nums_sum = nums[0]
        re = n
        while i <= j and j < n:
            if nums_sum < s:
                nums_sum += nums[j]
                j += 1
                continue

            if j - i < re:
                re = j - i

            nums_sum -= nums[i]
            i += 1

        while i <= j and nums_sum - nums[i] >= s:
            nums_sum -= nums[i]
            re -= 1
            i += 1

        return re

    def minSubArrayLen1(self, s, nums):
        # 此种方法不推荐，感觉这不是正常思维
        n = len(nums)
        res = n + 1
        nums_sum = 0
        l = 0
        r = -1 # 滑动窗口为nums[l, r]
        while l < n:
            if r + 1 < n and nums_sum < s:
                r += 1
                nums_sum += nums[r]
            else:
                nums_sum -= nums[l]
                l += 1

            if nums_sum >= s:
                res = min(res, r - l + 1)

        if res == n+1:
            return 0
        else:
            return res



if __name__ == "__main__":
    so = Solution()
    s = 213
    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    re = so.minSubArrayLen(s, nums)
    print(re)

