#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 不能完全运行通过
class Solution:
    class __Freq:
        def __init__(self,value=None,freq=None):
            self.value = value
            self.freq = freq
        def cmp1(self,another):
            return self.freq <= another.freq

    class PriorityQueue():
        class MaxHeap():
            class Array(object):

                # 构造函数，传入数组的容量capacity构造array
                # 无参数的构造函数，默认数组的容量capacity=10
                def __init__(self, capacity=10, arr=None):
                    if arr == None:
                        self.__data = [None] * capacity
                        self.__size = 0
                    else:
                        self.__data = arr
                        self.__size = len(arr)

                # 获取数组中元素的个数
                def getSize(self):
                    return self.__size

                # 获取数组的容量
                def getCapacity(self):
                    return len(self.__data)

                # 返回数组是否为空
                def isEmpty(self):
                    return self.__size == 0

                # 向所有元素后添加一个新元素
                # def addLast(self, e):
                #     assert self.__size < len(self.__data), "addLast is failed. Array is full"
                #     self.__data[self.__size] = e
                #     self.__size += 1

                # 向所有元素后添加一个新元素 也可以调用add方法
                def addLast(self, e):
                    self.add(self.__size, e)

                # 同理，也可以调用add 向数组的开始添加一个元素
                def addFirst(self, e):
                    self.add(0, e)

                # 向指定的位置添加元素
                def add(self, index, e):
                    # assert self.__size < len(self.__data), "add is failed. Array is full"
                    assert (index >= 0) and (index <= self.__size), \
                        "add is failed. Required index >= 0 and index <= size"
                    # 动态数组，如果self.__size == len(self.__data) 扩容为原来数组的两倍
                    if self.__size == len(self.__data):
                        self.__resize(len(self.__data) * 2)

                    i = self.__size - 1
                    while i >= index:
                        self.__data[i + 1] = self.__data[i]
                        i -= 1
                    self.__data[index] = e
                    self.__size += 1

                # 获取index索引位置的元素
                def get(self, index):
                    assert (index >= 0) and (index < self.__size), "Get failed, index is Illegal."
                    return self.__data[index]

                # 修改index索引位置的元素为e
                def set(self, index, e):
                    assert (index >= 0) and (index < self.__size), "Get failed, index is Illegal."
                    self.__data[index] = e

                # 查找数组中是否存在元素e
                def contains(self, e):
                    for i in range(self.__size):
                        if self.__data[i] == e:
                            return True
                    return False

                # 查找数组中是否存在e，若存在，返回存在的个数，若不存在返回0
                def containsCount(self, e):
                    count = 0
                    for i in range(self.__size):
                        if self.__data[i] == e:
                            count += 1
                    return count

                # 查找数组中元素e所在的索引，如果不存在元素e，则返回-1
                def find(self, e):
                    for i in range(self.__size):
                        if self.__data[i] == e:
                            return i
                    return -1

                # 查找数组中元素e所在的位置的所有索引（数组中可能包含多个e），若不存在元素e，返回-1
                def findAll(self, e):
                    indexs = []
                    for i in range(self.__size):
                        if self.__data[i] == e:
                            indexs.append(i)
                    if len(indexs) == 0:
                        return -1
                    else:
                        return indexs

                # 从数组中删除index位置的元素，返回被删除的元素
                def remove(self, index):
                    assert (index >= 0) and (index < self.__size), "remove failed, index is illegal"
                    # if self.__size <= len(self.__data)/2:
                    # lazy ,优化时间复杂度
                    if self.__size <= len(self.__data) / 4:
                        self.__resize(int(len(self.__data) / 2))
                    ret = self.__data[index]
                    for i in range(index, self.__size - 1):
                        self.__data[i] = self.__data[i + 1]
                    self.__size -= 1
                    return ret

                # 删除第一个元素
                def removeFirst(self):
                    self.remove(0)

                # 删除最后一个元素
                def removeLast(self):
                    self.remove(self.__size - 1)

                # 若数组中含有元素e,则删除一个
                def removeElement(self, e):
                    index = self.find(e)
                    if index != -1:
                        self.remove(index)

                # 若数组中含有元素e，删除掉所有的元素e
                def removeAllElement(self, e):
                    indexs = self.findAll(e)
                    temp = 0
                    if indexs != -1:
                        for i in indexs:
                            self.remove(i - temp)
                            temp += 1

                def __resize(self, newCapacity):
                    newarr = [None] * newCapacity
                    for i in range(self.__size):
                        newarr[i] = self.__data[i]
                    self.__data = newarr

                def swap(self, index1, index2):
                    self.__data[index1], self.__data[index2] = self.__data[index2], self.__data[index1]

                def __str__(self):
                    res = 'Array: size = %d, capacity = %d\n' % (self.__size, len(self.__data))
                    res += '['
                    for i in range(self.__size):
                        res += str(self.__data[i])
                        if i != self.__size - 1:
                            res += ', '
                    res += ']'
                    return res

            def __init__(self, capacity=10):
                self.data = self.Array(capacity)

            def getSize(self):
                return self.data.getSize()

            def isEmpty(self):
                return self.data.isEmpty()

            def __parent(self, index):
                return (index - 1) // 2

            def __leftChild(self, index):
                return index * 2 + 1

            def __rightCild(self, index):
                return index * 2 + 2

            def add(self, e):
                self.data.addLast(e)
                self.__SlipUp(self.getSize() - 1, e)

            def __SlipUp(self, k, e):
                while k > 0 and e.cmp1(self.data.get(self.__parent(k))):
                    self.data.swap(k, self.__parent(k))
                    k = self.__parent(k)

            def findMax(self):
                assert self.getSize() != 0, "The maxHeap must not be empty"
                return self.data.get(0)

            def extractMax(self):
                re = self.data.get(0)
                # self.data.set(0, self.data.get(self.getSize()-1))
                self.data.swap(0, self.getSize() - 1)
                self.data.removeLast()
                self.__siftDown(0)

                return re

            def __siftDown(self, k):

                while (self.__leftChild(k) < self.getSize()):
                    j = self.__leftChild(k)
                    if j + 1 < self.getSize() and self.data.get(j).cmp1(self.data.get(j+1)):
                        j += 1
                    # j 为k 左右孩子中数值较大的孩子

                    if self.data.get(k) < self.data.get(j):
                        self.data.swap(k, j)
                        k = j
                    else:
                        break

            # 取出堆中最大的元素，并替换成元素e
            def replace(self, e):
                maxValue = self.findMax()
                self.data.set(0, e)
                self.__siftDown(0)
                return maxValue

            # 把一个数组 构造成最大堆
            def heapify(self, arr):
                self.data = self.Array(arr=arr)
                # 从最后一个不是叶子节点的节点开始下沉，即最后一个叶子节点的父节点
                k = self.__parent(self.getSize() - 1)
                while k >= 0:
                    self.__siftDown(k)
                    k -= 1

            def __str__(self):
                res = '['
                for i in range(self.getSize()):
                    res += str(self.data.get(i))
                    if i != self.getSize() - 1:
                        res += ', '
                res += ']'
                return res

        def __init__(self):
            self.maxHeap = self.MaxHeap()

        def getSize(self):
            return self.maxHeap.getSize()

        def isEmpty(self):
            return self.maxHeap.isEmpty()

        def getFront(self):
            return self.maxHeap.findMax()

        def enqueue(self, e):
            self.maxHeap.add(e)

        def dequeue(self):
            return self.maxHeap.extractMax()

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

        pq = self.PriorityQueue()
        for key in dict_num.keys():
            if pq.getSize() < k:
                pq.enqueue(self.__Freq(key, dict_num[key]))
                continue

            if pq.getFront().freq < dict_num[key]:
                pq.dequeue()
                pq.enqueue(self.__Freq(key, dict_num[key]))
        re = []
        while pq.isEmpty() is not True:
            re.insert(0, pq.dequeue().value)
        return re
if __name__ == '__main__':
    so = Solution()
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    # nums = [1]
    # k = 1
    re = so.topKFrequent(nums, k)
    print(re)










