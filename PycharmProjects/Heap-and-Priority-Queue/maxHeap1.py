#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myarray import Array
#基于数组实现最大堆
class MaxHeap():
    def __init__(self,capacity=10):
        self.data = Array(capacity)

    def getSize(self):
        return self.data.getSize()

    def isEmpty(self):
        return self.data.isEmpty()

    def __parent(self,index):
        return (index-1)//2

    def __leftChild(self,index):
        return index*2 + 1

    def __rightCild(self,index):
        return index*2 + 2

    def add(self,e):
        self.data.addLast(e)
        self.__SlipUp(self.getSize()-1,e)

    def __SlipUp(self,k,e):
        while k>0 and e >self.data.get(self.__parent(k)):
            self.data.swap(k,self.__parent(k))
            k = self.__parent(k)

    def findMax(self):
        assert self.getSize() != 0, "The maxHeap must not be empty"
        return self.data.get(0)

    def extractMax(self):
        re = self.data.get(0)
        # self.data.set(0, self.data.get(self.getSize()-1))
        self.data.swap(0, self.getSize()-1)
        self.data.removeLast()
        self.__siftDown(0)

        return re

    def __siftDown(self,k):

        while(self.__leftChild(k) < self.getSize()):
            j = self.__leftChild(k)
            if j+1 < self.getSize() and self.data.get(j+1) >self.data.get(j):
                j += 1
            # j 为k 左右孩子中数值较大的孩子
            if self.data.get(j) > self.data.get(k):
                self.data.swap(k,j)
                k = j
            else:
                break
    # 取出堆中最大的元素，并替换成元素e
    def replace(self,e):
        maxValue = self.findMax()
        self.data.set(0, e)
        self.__siftDown(0)
        return maxValue

    # 把一个数组 构造成最大堆
    def heapify(self, arr):
        self.data = Array(arr = arr)
        # 从最后一个不是叶子节点的节点开始下沉，即最后一个叶子节点的父节点
        k = self.__parent(self.getSize()-1)
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


if __name__ == '__main__':
    maxheap = MaxHeap()
    for i in [62, 41, 28, 30, 22, 13, 19, 17, 15, 16]:
        maxheap.add(i)
    print(maxheap)

    maxheap1 = MaxHeap()
    maxheap1.heapify([62, 41, 28, 30, 22, 13, 19, 17, 15, 16])
    print(maxheap1)

    maxheap1.replace(10)
    print(maxheap1)
