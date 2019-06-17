# timeOut

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_muns = [0] * (len(nums) + 1)
        for k in range(len(nums)):
            self.sum_muns[k + 1] = self.sum_muns[k] + nums[k]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        dif = val - self.nums[i]
        self.nums[i] = val
        self.sum_muns[i+1:] = [x+dif for x in self.sum_muns[i+1 :]]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_muns[j+1] - self.sum_muns[i]

if __name__ == "__main__":
    # nums = [-2, 0, 3, -5, 2, -1]
    nums = [7,2,7,2,0]
    so = NumArray(nums)
    so.update(4,6)
    so.update(0,2)
    so.update(0,9)
    re1 = so.sumRange(4, 4)
    print(re1)
    so.update(3,8)
    re1 = so.sumRange(0, 4)
    print(re1)
    so.update(4, 1)
    re1 = so.sumRange(0, 3)
    print(re1)
    re1 = so.sumRange(0, 4)
    print(re1)





