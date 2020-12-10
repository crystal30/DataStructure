from functools import cmp_to_key

# 这个方法有用例解答错误，看一下是为什么？
class Solution:
    def eraseOverlapIntervals(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return 0

        # memo[i]表示从memo[0——i]需要移除掉区间的最小数量
        memo = [0 for _ in range(len_intervals)]
        memo_interval = []
        memo_interval.append(intervals[0])
        for i in range(1, len_intervals):
            over_laps = []  # 存储 intervals[i] 和 之前重复的interval
            for interval_range in memo_interval:
                # 表示 intervals[i] 不在之前的范围内
                if intervals[i][1] <= interval_range[0] or intervals[i][0] >= interval_range[1]:
                    pass
                else:
                    over_laps.append(interval_range)
            len_over_laps= len(over_laps)
            if len_over_laps == 0:
                memo[i] = memo[i-1]
                memo_interval.append(intervals[i])
            elif len_over_laps >= 2:
                memo[i] = memo[i-1] + 1
            else: # len_re == 1
                memo[i] = memo[i - 1] + 1
                intervals_i = intervals[i][1] - intervals[i][0]
                pre_interval = over_laps[0][1] - over_laps[0][0]
                if intervals_i < pre_interval:
                    memo_interval.remove(over_laps[0])
                    memo_interval.append(intervals[i])

        return memo[len_intervals-1]

# 动态规划
class Solution1:
    def eraseOverlapIntervals(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return 0

        intervals_sort = sorted(intervals, key=lambda t:t[0])
        # mmeo[i] 表示把第i个interval放进去，最长的区间
        memo = [1 for _ in range(len_intervals)]

        for i in range(1, len_intervals):
            intervals_i0 = intervals_sort[i][0]
            memo_i_list = [1]
            for j in range(i):
                # 因为是intervals 是已经排过序的，所以，只要保证如下，就说明，不是在重复的区间
                if intervals_i0 >= intervals_sort[j][1]:
                    memo_i_list.append(1+memo[j])

            memo[i] = max(memo_i_list)
        return len_intervals-max(memo)


# 动态规划
class Solution2:
    def eraseOverlapIntervals(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return 0

        intervals_sort = sorted(intervals, key=lambda t:t[1])
        # mmeo[i] 表示把第i个interval放进去，最长的区间
        memo = [1 for _ in range(len_intervals)]

        for i in range(1, len_intervals):
            intervals_i0 = intervals_sort[i][0]
            memo_i_list = [1]
            for j in range(i):
                # 因为是intervals 是已经排过序的，所以，只要保证如下，就说明，不是在重复的区间
                if intervals_i0 >= intervals_sort[j][1]:
                    memo_i_list.append(1+memo[j])
                else:
                    break
            memo[i] = max(memo_i_list)

        return len_intervals-max(memo)


# 贪心算法
class Solution3:
    def __cmpare(self, interval_1, interval_2):
        if interval_1[1] != interval_2[1]:
            return interval_1[1] - interval_2[1]
        else:
            return interval_1[0] - interval_2[0]

    def eraseOverlapIntervals(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return 0
        intervals_sort = sorted(intervals, key=cmp_to_key(self.__cmpare))
        re = 1
        pre = 0
        for i in range(1, len_intervals):
            if intervals_sort[i][0] >= intervals_sort[pre][1]:
                re += 1
                pre = i
        return len_intervals - re


# 贪心算法


if __name__ == "__main__":
    so = Solution3()
    intervals = [ [1,3], [2,3], [3,4], [1,2] ]
    re = so.eraseOverlapIntervals(intervals)
    print(re)






