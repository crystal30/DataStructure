class Solution:
    def findDuplicate(self, nums):
        nums.sort()
        len_nums = len(nums)
        for i in range(len_nums - 1):
            if nums[i] == nums[i+1]:
                return nums[i]

if __name__ == '__main__':
    so = Solution()
    nums = [1,1,2]
    re = so.findDuplicate(nums)
    print(re)