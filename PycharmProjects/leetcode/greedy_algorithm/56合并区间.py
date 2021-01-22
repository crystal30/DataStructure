class Solution:
    def merge(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return intervals

        intervals.sort(key=lambda t: t[0])
        re = []
        pre_i = intervals[0][0]
        pre_j = intervals[0][1]
        for i in range(1, len_intervals):
            new_i = intervals[i][0]
            new_j = intervals[i][1]
            if pre_i == new_i:
                if pre_j < new_j:
                    pre_j = new_j
            elif pre_i < new_i:
                if pre_j >= new_i:
                    if pre_j < new_j:
                        pre_j = new_j
                else:
                    re.append([pre_i, pre_j])
                    pre_i = new_i
                    pre_j = new_j
        re.append([pre_i, pre_j])
        return re


## 少点if else？
class Solution1:
    def merge(self, intervals):
        len_intervals = len(intervals)
        if len_intervals <= 1:
            return intervals

        intervals.sort(key=lambda t: t[0])
        re = []
        pre_i = intervals[0][0]
        pre_j = intervals[0][1]
        for i in range(1, len_intervals):
            new_i = intervals[i][0]
            new_j = intervals[i][1]
            if pre_i == new_i and pre_j < new_j:
                pre_j = new_j
                continue
            if pre_i < new_i and pre_j >= new_i and pre_j < new_j:
                pre_j = new_j
                continue
            if pre_j < new_i:
                re.append([pre_i, pre_j])
                pre_i = new_i
                pre_j = new_j

        re.append([pre_i, pre_j])
        return re

if __name__ == "__main__":
    so = Solution()
    intervals = [[1,3], [1,4], [3,6], [2,4], [3,5]]
    re = so.merge(intervals)
    print(re)
