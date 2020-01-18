class Solution:
    def __init__(self):
        self.re = []

    def permute(self, nums):
        self.sub_permute(nums, 0, [])
        return self.re

    def sub_permute(self, nums, index, sub_re):

        len_nums = len(nums)
        if index == len_nums:
            if sub_re != []:
                self.re.append(sub_re)
            return

        temp = sub_re.copy()
        temp.append(nums[index])

        sub_nums = nums.copy()
        sub_nums.pop(index)

        self.sub_permute(sub_nums, 0, temp)

        if index + 1 < len_nums:
            self.sub_permute(nums, index+1, sub_re)
        return
if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3]
    re = so.permute(nums)
    print(re)
