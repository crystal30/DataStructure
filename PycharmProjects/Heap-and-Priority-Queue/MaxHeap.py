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

    # 假设 index 是从0开始的
    def __parent(self,index):
        return (index-1)//2

    def __leftChild(self,index):
        return index*2 + 1

    def __rightCild(self,index):
        return index*2 + 2

    def add(self,e):
        self.data.add(self.getSize(), e)
        child = self.getSize()-1
        parent = self.__parent(self.getSize()-1)
        if parent>0:
            while e > self.data.get(parent):
                temp = self.data.get(parent)
                self.data.set(parent, e)
                self.data.set(child,temp)
                child = parent
                parent = self.__parent(parent)

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
    print(maxheap.getSize())
    print(maxheap.isEmpty())
    for i in [62,41,30,28,16,22,13,19,17,15]:
        maxheap.add(i)
    print(maxheap.getSize())
    print(maxheap.isEmpty())
    print(maxheap)
    maxheap.add(52)
    print(maxheap)
