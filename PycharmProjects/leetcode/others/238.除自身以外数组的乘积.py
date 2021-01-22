class Solution:
    def productExceptSelf(self, nums):
        len_nums = len(nums)
        pre_nums = [0 for _ in range(len_nums-1)]
        after_nums = [0 for _ in range(len_nums)]
        ac = 1
        for i in range(len_nums - 1):
            ac *= nums[i]
            pre_nums[i] = ac

        ac = 1
        for i in range(len_nums - 1, 0, -1):
            ac *= nums[i]
            after_nums[i] = ac

        re_nums = [0 for _ in range(len_nums)]
        for i in range(1, len_nums-1):
            re_nums[i] = pre_nums[i-1] * after_nums[i+1]

        re_nums[0] = after_nums[1]
        re_nums[len_nums-1] = pre_nums[len_nums - 2]
        return re_nums

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3,4]
    re = so.productExceptSelf(nums)
    print(re)





