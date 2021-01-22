class Solution:
    def searchRange(self, nums, target):
        len_nums = len(nums)
        if len_nums == 0:
            return [-1, -1]
        i = 0
        j = len_nums - 1
        re = [-1, -1]
        while i <= j:
            if target > nums[i]:
                i += 1
            elif target == nums[i]:
                re[0] = i
            else:
                break
            if target < nums[j]:
                j -= 1
            elif target == nums[j]:
                re[1] = j
            else:
                break
            if re[0] != -1 and re[1] != -1:
                return re
        return re


if __name__ == '__main__':
    nums = [1]
    target = 1
    so =Solution()
    re = so.searchRange(nums, target)
    print(re)
