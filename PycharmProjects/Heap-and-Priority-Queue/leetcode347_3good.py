# -*- coding: utf-8 -*-
from collections import Counter
class MaxHeap():
    def __init__(self):
        self.__data = []

    def getSize(self):
        return len(self.__data)

    def isEmpty(self):
        return self.__data == []

    # 假设 index 是从0开始的
    def __parent(self, index):
        return (index - 1) // 2

    def __leftChild(self, index):
        return index * 2 + 1

    def __rightCild(self, index):
        return index * 2 + 2

    # #实现最大堆
    # def cmp(self,a,b):
    #     return a>b

    #解决 leetcode347
    def cmp(self,item1, item2):
        return item1.freq < item2.freq

    def add(self,e):
        self.__data.append(e)
        self.__slipUp(self.getSize()-1)

    def __slipUp(self,k):
        parent = self.__parent(k)
        while parent >= 0:
            if self.cmp(self.__data[k], self.__data[parent]):
                self.__swap(k, parent)
                k = parent
                parent = self.__parent(k)
            else:
                break

    def extraMax(self):
        re = self.__data[0]
        self.__data[0] = self.__data[self.getSize()-1]
        self.__data.pop()
        self.__slipDown(0)
        return re

    def __slipDown(self,p):
        while self.__leftChild(p)< self.getSize():
            child = self.__leftChild(p)
            # child 为左孩子， child + 1 即为右孩子
            if child+1 <self.getSize() and self.cmp(self.__data[child+1], self.__data[child]):
                child += 1
            if self.cmp(self.__data[child],self.__data[p]):
                self.__swap(p, child)
                p = child
            else:
                break

    def __swap(self,a,b):
        self.__data[a],self.__data[b] = self.__data[b], self.__data[a]

    def findMax(self):
        return self.__data[0]

    def heapify(self,arr):
        self.__data = arr
        n = self.__parent(self.getSize()-1)
        while n >= 0:
            self.__slipDown(n)
            n -= 1
        return self

    # 取出堆中最大的(优先级最高的)元素，并替换成元素e
    def replace(self,e):
        re = self.__data[0]
        self.__data[0] = e
        self.__slipDown(0)
        return re

    def __getitem__(self, item):
        return self.__data[item]

    def __str__(self):
        return str(self.__data)

class PriorityQueue():
    def __init__(self):
        self.__data = MaxHeap()

    def isEmpty(self):
        return self.__data.isEmpty()

    def getSize(self):
        return self.__data.getSize()

    def getFront(self):
        return self.__data.findMax()

    def enqueue(self,e):
        return self.__data.add(e)

    def dequeue(self):
        return self.__data.extraMax()

    def __getitem__(self, item):
        return self.__data[item]

class Freq:
    def __init__(self,v,freq):
        self.v = v
        self.freq = freq

class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_freq = Counter(nums)
        pq = PriorityQueue()
        re = [None]*k
        for num,freq in num_freq.items():
            if pq.getSize() < k:
                pq.enqueue(Freq(num, freq))
                continue

            if pq.getFront().freq < freq:
                pq.dequeue()
                pq.enqueue(Freq(num, freq))

        while k-1 >=0:
            re[k-1] = pq.dequeue().v
            k -= 1
        return re

if __name__ == '__main__':
    so = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    re = so.topKFrequent(nums, k)
    print(re)




