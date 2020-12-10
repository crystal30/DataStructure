class Solution:
    def __init__(self):
        self.len_nums = 0
        self.memo = None

    def jump(self, nums):
        self.len_nums = len(nums)
        if self.len_nums <= 1:
            return 0

        self.memo = [None for _ in range(self.len_nums)]
        for index, num in enumerate(nums):
            if num >= self.len_nums - index - 1:
                self.memo[index] = 1
        return self._can_jump(nums, 0)

    def _can_jump(self, nums, start_i):
        if start_i == self.len_nums - 1:
            return 0

        if self.memo[start_i] is not None:
            return self.memo[start_i]

        times_list = []
        step_range = min(self.len_nums - start_i, nums[start_i] + 1)
        for step in range(1, step_range):
            times_list.append(self._can_jump(nums, start_i + step))

        if len(times_list) == 0:
            min_times = 10000000000000
        else:
            min_times = min(times_list)

        self.memo[start_i] = 1 + min_times
        return 1 + min_times


# 动态规划的方法
class Solution1:
    def jump(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        memo = [-1 for _ in range(len_nums)]
        for index, num in enumerate(nums):
            if num >= len_nums - index - 1:
                memo[index] = 1
        memo[-1] = 0
        for i in range(len_nums-2, -1, -1):
            step_range = min(nums[i]+1, len_nums-i)
            times_list = []
            for step in range(1, step_range):
                times_list.append(memo[i + step])

            if len(times_list) == 0:
                min_times = 10000000000
            else:
                min_times = 1 + min(times_list)
            memo[i] = min_times

        return memo[0]


# 用贪心算法
class Solution2:
    def jump(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return 0

        index = len_nums - 1
        times = 0
        while index >= 0:
            if index == 0:
                return times
            for num_i in range(index):
                if nums[num_i] >= index - num_i:
                    index = num_i
                    times += 1
                    break
        return times


# 贪心算法2，比较难理解
class Solution3:
    def jump(self, nums):
        len_nums = len(nums)
        if len_nums == 1:
            return 0

        max_reach = 0
        times = 0
        end = 0
        for num_i, num in enumerate(nums):
            # 因为题目中已经说明了肯定可以到达最后一个位置，故不再需要 判断 num_i>max_reach
            max_reach = max(max_reach, num_i + num)
            if num_i == end:
                times += 1
                end = max_reach
            if end == len_nums - 1:
                return times

if __name__ == "__main__":
    so = Solution3()
    nums = [2,3,1,1,4]
    re = so.jump(nums)
    print(re)