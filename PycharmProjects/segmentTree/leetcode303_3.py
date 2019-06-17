# AC
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_muns = [0] * (len(nums) + 1)
        for k in range(len(nums)):
            self.sum_muns[k + 1] = self.sum_muns[k] + nums[k]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_muns[j+1] - self.sum_muns[i]

# timeOut, why?

class NumArray1:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)
        self.sum_muns = [0] * (self.n + 1)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        for k in range(self.n):
            self.sum_muns[k + 1] = self.sum_muns[k] + self.nums[k]
        return self.sum_muns[j+1] - self.sum_muns[i]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    so = NumArray1(nums)
    re = so.sumRange(0,2)
    print(re)