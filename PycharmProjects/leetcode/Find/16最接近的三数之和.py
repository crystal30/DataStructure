class Solution:
    #204ms
    #时间复杂度：O(n2)
    #空间复杂度：O(1)
    #思路同15题的思路
    #a = nums[i], b = nums[j], c = nums[k],
    # 先固定住a，然后采用对撞指针的方式找出nums[j],nums[k]
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        residual = float('inf')
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                if nums[i] + nums[j] + nums[k]>target:
                    new_residual = abs(nums[i] + nums[j] + nums[k] - target)
                    if new_residual<residual:
                        residual = new_residual
                        re = nums[i] + nums[j] + nums[k]
                    k -= 1
                elif nums[i] + nums[j] + nums[k]<target:
                    new_residual = abs(nums[i] + nums[j] + nums[k] - target)
                    if new_residual < residual:
                        residual = new_residual
                        re = nums[i] + nums[j] + nums[k]
                    j += 1
                else:
                    return target
        return re


    #对threeSumClosest的容余操作进行清除
    #时间复杂度仍同threeSumClosest，但是对代码改进后，速率提升很多
    #84ms
    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        residual = float('inf')
        for i in range(n - 2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > target:
                    new_residual = abs(total- target)
                    if new_residual < residual:
                        residual = new_residual
                        re = total
                    k -= 1
                elif total < target:
                    new_residual = abs(total - target)
                    if new_residual < residual:
                        residual = new_residual
                        re = total
                    j += 1
                else:
                    return target
        return re


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    so = Solution()
    re = so.threeSumClosest(nums, target)
    pass
