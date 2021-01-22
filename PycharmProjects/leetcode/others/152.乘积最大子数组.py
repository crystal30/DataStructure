# 最后一个用例超出时间限制，有没有什么更好的做法？
class Solution:
    def maxProduct(self, nums):
        len_nums = len(nums)
        # 根据题意，len_nums 不为0
        if len_nums == 1:
            return nums[0]
        if len_nums == 2:
            return max(nums[0], nums[1], nums[0]*nums[1])

        memo = [-1 for _ in range(len_nums)]
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1], nums[0]*nums[1])

        for i in range(2, len_nums):
            max_value = nums[i]
            pre_value = nums[i]
            for j in range(i-1,-1,-1):
                current_value = pre_value * nums[j]
                if current_value > max_value:
                    max_value = current_value
                pre_value = current_value

                if nums[j] == 0:
                    break

            memo[i] = max(memo[i-1], max_value)

        return memo[len_nums-1]

class Solution1:
    def maxProduct(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        min_value = 1
        max_value = 1
        re = 0
        for i in range(len_nums):
            if nums[i] < 0:
                min_value, max_value = max_value, min_value
            max_value = max(max_value * nums[i], nums[i])
            if max_value > re:
                re = max_value
            min_value = min(min_value * nums[i], nums[i])
        return re



if __name__ == '__main__':
    so = Solution1()
    nums = [2,3,-2,4]
    re = so.maxProduct(nums)
    print(re)



