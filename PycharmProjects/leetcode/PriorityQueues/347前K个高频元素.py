# _*_ coding: utf-8 _*_

from collections import OrderedDict
from collections import Counter
import heapq
from queue import PriorityQueue

class Solution:
    # 有序字典法
    def topKFrequent(self, nums, k):
        nums.sort()
        nums_dict = OrderedDict()
        for num in nums:
            n = nums_dict.setdefault(num, 0)
            nums_dict[num] = n + 1

        nums_dict = sorted(nums_dict.items(), key = lambda t: t[1], reverse = True)

        re = []
        for i in range(k):
            re.append(nums_dict[i][0])

        return re
################################

class my_PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priprity):
        heapq.heappush(self._queue, (-priprity, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def size(self):
        return self._index

class Solution1:
    # 优先队列法
    def topKFrequent1_1(self, nums, k):
        nums.sort()
        nums_count = Counter(nums)
        pq = my_PriorityQueue()
        for e in nums_count.items():
            pq.push(e[0], e[1])

        re = []
        for _ in range(k):
            re.append(pq.pop())

        return re

    #???? 尝试一下维护长度为k的优先队列
    
if __name__ == "__main__":
    so = Solution1()
    # nums = [1,1,1,2,2,3]
    # nums = [3, 3, 2, 2, 1, 1, 1]
    # k = 2
    nums =[4, 1, -1, 2, -1, 2, 3]
    k = 2
    re = so.topKFrequent1_3(nums, k)
    print(re)