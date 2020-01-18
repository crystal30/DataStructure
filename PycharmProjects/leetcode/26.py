class Solution:
    def removeDuplicates(self, nums):
        len_nums = len(nums)
        k = 1 # nums[0,k) 中存放的是不重复的元素
        for i in range(1, len_nums):
            if nums[i] not in nums[0:k]:  # 感觉这里耗时比较长，优化？
                if i != k:
                    nums[k] = nums[i]
                k += 1
        return k

    # 对removeDuplicates 进行优化？
    # 注意：其是排序数组


if __name__ == "__main__":
    nums = [1,1,2]
    so = Solution()
    re = so.removeDuplicates(nums)
    print(re)
    pass


