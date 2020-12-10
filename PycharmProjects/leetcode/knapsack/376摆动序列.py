class Solution:
    def wiggleMaxLength(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums

        # memo[i][0]表示以i结尾，且nums[i]小于前一个数，memo[i][1]表示以i结尾，且nums[i]大于前一个数
        memo = [[1, 1] for _ in range(len_nums)]
        for i in range(1, len_nums):
            for j in range(i):
                if nums[i] < nums[j]:
                    memo[i][0] = max(memo[i][0], 1 + memo[j][1])
                elif nums[i] > nums[j]:
                    memo[i][1] = max(memo[i][1], 1 + memo[j][0])
        res = 1
        for i in range(len_nums):
            res = max(res, memo[i][0], memo[i][1])

        return res

if __name__ == "__main__":
    so = Solution()
    nums = [0,0]
    re = so.wiggleMaxLength(nums)
    print(re)