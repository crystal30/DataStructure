class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        n = len(nums)
        re = []
        if n < 4:
            return []
        if n == 4:
            if sum(nums) != target:
                return []
            else:
                re.append(nums)
                return re

        for i in range(n-3):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                m = n -1
                while k < m:
                    sum_t = nums[i] + nums[j] + nums[k] + nums[m]
                    if sum_t > target:
                        m -= 1
                        while m > 2 and nums[m] == nums[m + 1]:
                            m -= 1
                    elif sum_t < target:
                        k += 1
                        while k < n - 2 and nums[k] == nums[k - 1]:
                            k += 1
                    else:
                        re.append([nums[i], nums[j], nums[k], nums[m]])
                        m -= 1
                        while m > 2 and nums[m] == nums[m + 1]:
                            m -= 1

                        k += 1
                        while k < n - 2 and nums[k] == nums[k - 1]:
                            k += 1

        return re

if __name__ == "__main__":
    so = Solution()
    nums = [-1,0,1,2,-1,-4]
    target = -1
    re = so.fourSum(nums, target)
    print(re)




