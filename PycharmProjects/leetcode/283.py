class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0
        n = 0
        while n < len_nums:
            if nums[i] == 0:
               nums.pop(i)
               nums.append(0)
            else:
               i += 1

            n += 1

    def moveZeroes1(self, nums):
        len_nums = len(nums)
        k = 0 # [0,k)存放非0元素的位置
        if len_nums > 1:
            for i in range(len_nums):
                if nums[i] != 0:
                    if k != i:
                        nums[k] = nums[i]
                        k += 1
                    else:
                        k += 1

            for j in range(k, len_nums):
                nums[j] = 0

    # 0元素与非0元素交换位置
    def moveZeroes2(self, nums):
        len_nums = len(nums)
        k = 0 # [0,k)存放非0元素的位置
        for i in range(len_nums):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


if __name__ == "__main__":
    nums = [1,0]
    so = Solution()
    so.moveZeroes2(nums)
    print(nums)
    pass




