class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums == 1:
            return nums
        # 看一下长度为2的适用否？
        i = len_nums - 2
        k_stack = []
        while i >= 0:
            k = -1
            for j in range(i+1, len_nums):
                k = find_k(nums, i, j, k)
            if k != -1:
                nums[i], nums[k] = nums[k], nums[i]
                sub_nums = nums[i+1:len_nums]
                sub_nums.sort()
                nums[i + 1:len_nums] = sub_nums[::]
                return nums
            i -= 1
        nums.sort()
        return nums
def find_k(nums, i, j, k):
    if nums[j] > nums[i]:
        if k == -1:
            k = j
        else:
            if nums[k] > nums[j]:
                k = j
    return k


if __name__ == '__main__':
    so = Solution()
    nums = [1,3,2]
    re = so.nextPermutation(nums)
    print(re)