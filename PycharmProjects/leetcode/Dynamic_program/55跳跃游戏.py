# 递归，超出时间限制，剩下最后一个用例没有通过
class Solution:
    def __init__(self):
        self.len_nums = 0
        self.memo = None
    def canJump(self, nums):
        self.len_nums = len(nums)
        if self.len_nums <= 1:
            return True

        self.memo = [None for _ in range(self.len_nums)]
        return self._can_jump(nums, 0)

    def _can_jump(self, nums, start_i):
        if start_i == self.len_nums - 1:
            return True

        if self.memo[start_i] is not None:
            return self.memo[start_i]

        step_range = min(self.len_nums - start_i, nums[start_i] + 1)
        for step in range(1, step_range):
            if self._can_jump(nums, start_i + step):
                self.memo[start_i] = True
                return True

        self.memo[start_i] = False
        return False

# 动态规划 最后一个用例超时间
class Solution1:
    def canJump(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return True

        memo = [False for _ in range(len_nums)]
        memo[-1] = True
        for i in range(len_nums-1, -1, -1):
            step_range = min(nums[i] + 1, len_nums - i)
            for step in range(step_range-1,0,-1):
                if memo[i+step]:
                    memo[i] = True
                    break

        return memo[0]


# 贪心算法
class Solution2:
    def canJump(self, nums):
        # 根据题意，可知，测试用例没有空数组
        len_nums = len(nums)
        if len_nums == 1:
            return True

        index = len_nums - 1
        new_index = index
        while index >= 0:
            if index == 0:
                return True
            for num_i in range(index):
                if nums[num_i] >= index - num_i:
                    new_index = num_i
                    break
            if new_index != index:
                index = new_index
            else:
                return False

# 贪心算法2，但感觉不是很好理解
class Solution3:
    def canJump(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return True

        max_reach = 0
        for num_i , num in enumerate(nums):
            if num_i > max_reach:
                return False
            max_reach = max(max_reach, num_i + num)
            if max_reach >= len_nums - 1:
                return True



if __name__ == "__main__":
    so = Solution3()
    nums = [1,1,0,2,1]
    re = so.canJump(nums)
    print(re)

