class Solution:
    def removeElement(self, nums, val):
        k = 0  #nums[0,k)存放的为该保留下来的元素
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] != val:
                if i != k:
                    nums[k] = nums[i]
                k += 1

        return k

    # 优化？

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]

    val = 2
    so = Solution()
    re = so.removeElement(nums, val)
    print(re)
    pass