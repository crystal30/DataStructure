class Solution:
    def __init__(self):
        self.res = []
        self.used = None
    def permuteUnique(self, nums):
        len_nums = len(nums)
        self.used = [False] * len_nums
        self.generationPermuteUnique(nums, 0, [])
        return list(self.res)

    # nums 即要求全排列的数组
    # index 目前temp中有多少个数字
    # temp
    def generationPermuteUnique(self, nums, index, temp):
        len_nums = len(nums)
        if index == len_nums:
            if temp not in self.res:
                self.res.append(temp.copy())
            return

        for i in range(len_nums):
            if self.used[i] == False:
                temp.append(nums[i])
                self.used[i] = True
                self.generationPermuteUnique(nums, index+1, temp)
                temp.pop()
                self.used[i] = False
        return

    # 用自己比较理解的第二种方法做一下
    

if __name__ == "__main__":
    so = Solution()
    nums = [1,1,2]
    re = so.permuteUnique(nums)
    print(re)

