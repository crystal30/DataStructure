class Solution:
    def rob(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        if len_nums <= 2:
            return max(nums)

        memo = [-1] * len_nums
        memo[-1] = nums[-1]
        memo[-2] = nums[-2]

        memo1 = [-1] * len_nums
        memo1[-2] = nums[-2]
        memo1[-3] = nums[-3]

        index = list(range(1, len_nums - 2))
        for i in index[::-1]:
            memo[i] = nums[i] + max(memo[i + 2:])

        index1 = list(range(len_nums - 3))
        for i in index1[::-1]:
            memo1[i] = nums[i] + max(memo1[i + 2:])

        memo[0] = memo1[0]
        return max(memo)

#### 用其他方法尝试以下呢，感觉上一种方法还是比较笨的
class Solution4:
    def __init__(self):
        self.len_nums = 0
        self.memo = None

    def rob(self, nums):
        len_nums = len(nums)
        if len_nums <= 3:
            return max(nums)

        self.memo = [-1 for _ in range(len_nums)]
        money_memo = [None for _ in range(len_nums)]
        for i in range(1, len_nums):
            money_memo[i] = self._rob(i, nums)

        self.memo = [-1 for _ in range(len_nums)]
        money_memo[0] = self._rob(0, nums[:-1])
        return max(money_memo)


    def _rob(self, start_i, nums):
        len_nums = len(nums)
        if self.memo[start_i] != -1:
            return self.memo[start_i]

        if start_i >= len(nums) - 2:
            self.memo[start_i] = nums[start_i]
            return self.memo[start_i]

        max_money = []
        for i in range(start_i+2, len_nums):
            max_money.append(self._rob(i, nums))

        self.memo[start_i] = nums[start_i] + max(max_money)
        return self.memo[start_i]


class Solution5:
    def rob(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums <= 3:
            return max(nums)

        memo = [-1 for _ in range(len_nums)]
        memo[-1] = nums[-1]
        memo[-2] = nums[-2]
        memo[-3] = nums[-3]

        num_list = [i for i in range(len_nums-3)]
        # 肯定偷第一家
        for i in num_list[::-1]:
            max_money = []
            for j in range(i+2, len_nums-1):
                max_money.append(memo[j])

            memo[i] = nums[i] + max(max_money)

        # 将memo置位
        for i in range(1, len_nums-2):
            memo[i] = -1

        # 不偷第一家
        num_list = [i for i in range(1, len_nums - 2)]
        for i in num_list[::-1]:
            max_money = []
            for j in range(i + 2, len_nums):
                max_money.append(memo[j])

            memo[i] = nums[i] + max(max_money)

        return max(memo)


if __name__ == "__main__":
    so = Solution5()
    nums = []
    re = so.rob(nums)
    print(re)

