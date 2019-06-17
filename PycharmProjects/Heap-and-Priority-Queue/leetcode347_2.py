#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Queue import PriorityQueue

class Solution:
    class __Freq:
        def __init__(self,value=None,freq=None):
            self.value = value
            self.freq = freq
        def cmp(self,another):
            return self.freq <= another.freq

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
            if pq.qsize() < k:
                pq.put(self.__Freq(key,dict_num[key]))
                continue

            if pq.getFront().freq < dict_num[key]:
                pq.dequeue()
                pq.put(self.__Freq(key, dict_num[key]))
        re = []
        while pq.empty() is not True:
            re.insert(0,pq.get().value)
        return re
if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    re = so.topKFrequent(nums, k)
    print(re)