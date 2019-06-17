#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from priorityQueue import PriorityQueue
class Solution:
    class __Freq:
        def __init__(self,value=None,freq=None):
            self.value = value
            self.freq = freq
        def cmp(self,another):
            if self.freq > another.freq:
                return -1
            elif self.freq < another.freq:
                return 1
            else:
                return 0


    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_num = dict()
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1

        pq = PriorityQueue()
        for key in dict_num.keys():
            if pq.getSize() < k:
                pq.enqueue(self.__Freq(key,dict_num[key]))
                continue

            if pq.getFront().freq < dict_num[key]:
                pq.dequeue()
                pq.enqueue(self.__Freq(key, dict_num[key]))
        re = []
        while pq.isEmpty() is not True:
            re.insert(0,pq.dequeue().value)
        return re
if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    re = so.topKFrequent(nums, k)
    print(re)






