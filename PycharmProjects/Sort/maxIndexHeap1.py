#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
class MaxIndexHeap():
    def __init__(self):
        self.__data = []   #传入的数组，顺序一直是不变的
        self.__indexs = [] #传入的数组的索引 ，根据索引对应的数据，将索引变为最大堆
        self.__reverse = []  #表示索引i在堆中的位置（位置是从0开始的）
    def getSize(self):
        return len(self.__indexs)

    def isEmpty(self):
        return self.__indexs == []

    # 假设 index 是从0开始的
    def __parent(self, i):
        return (i - 1) // 2

    def __leftChild(self, i):
        return i * 2 + 1

    def __rightCild(self, i):
        return i * 2 + 2

    # #实现最大堆
    def cmp(self,a,b):
        return a>b

    #解决 leetcode347
    # def cmp(self,item1, item2):
    #     return item1.freq < item2.freq

    #由于加入了索引（可能是有意义的），所以我们插入时需要说明"索引" 和"元素的值"
    #默认的索引是从0开始的
    def add(self,i,e):
        self.__data.append(e)
        self.__indexs.append(i)
        self.__reverse.append(self.getSize()-1)
        self.__slipUp(self.getSize()-1)

    def __slipUp(self,k):
        parent = self.__parent(k)
        while parent >= 0:
            if self.cmp(self.__data[self.__indexs[k]], self.__data[self.__indexs[parent]]):
                self.__indexs[k], self.__indexs[parent] = self.__indexs[parent], self.__indexs[k]
                self.__reverse[self.__indexs[k]] = k
                self.__reverse[self.__indexs[parent]] = parent
                k = parent
                parent = self.__parent(k)
            else:
                break

    def extraMax(self):
        re = self.__data[self.__indexs[0]]
        self.__reverse[self.__indexs[0]] = None
        self.__indexs[0] = self.__indexs[self.getSize()-1]
        self.__reverse[self.__indexs[0]] = 0
        self.__indexs.pop()
        self.__slipDown(0)
        return re

    def extraMaxIndex(self):
        re = self.__indexs[0]
        self.__indexs[0] = self.__indexs[self.getSize()-1]
        self.__reverse[re] = None
        self.__reverse[self.__indexs[0]] = 0
        self.__indexs.pop()
        self.__slipDown(0)
        return re

    def __slipDown(self,p):
        while self.__leftChild(p)< self.getSize():
            child = self.__leftChild(p)
            # child 为左孩子， child + 1 即为右孩子
            if child+1 <self.getSize() and \
                    self.cmp(self.__data[self.__indexs[child+1]], self.__data[self.__indexs[child]]):
                child += 1
            if self.cmp(self.__data[self.__indexs[child]],self.__data[self.__indexs[p]]):
                self.__indexs[p], self.__indexs[child] = self.__indexs[child], self.__indexs[p]
                self.__reverse[self.__indexs[p]] = p
                self.__reverse[self.__indexs[child]] = child
                p = child
            else:
                break

    def findMax(self):
        return self.__data[self.__indexs[0]]

    def getItem(self, i):
        return self.__data[i]

    # 修改self.__data中下标为i的元素 的值 为newe
    #复杂度为O(n)+O(logn);其中遍历了一遍（for循环）是O(n)的，
    # 寻找到i在索引堆中的位置后，进行上浮或下沉操作的复杂度是O(logn)
    #如果要是对n个数值进行change，则需要O(n2)的复杂度，优化？
    def change(self, i, newe):
        self.__data[i] = newe
        for x in range(self.getSize()):
            # 假设最终的x为 i 在索引堆中的位置
            if self.__indexs[x] == i:
                self.__slipDown(x)
                self.__slipUp(x)
                return
    #对change1的改进
    def change1(self, i, newe):
        self.__data[i] = newe
        heap_pos = self.__reverse[i]
        self.__slipDown(heap_pos)
        self.__slipUp(heap_pos)
        return

    def heapify(self,arr):
        self.__data = copy.copy(arr)
        self.__indexs = [_ for _ in range(len(arr))]
        self.__reverse = [_ for _ in range(len(arr))]
        n = self.__parent(self.getSize()-1)
        while n >= 0:
            self.__slipDown(n)
            n -= 1
        return self

    # 取出堆中最大的(优先级最高的)元素，并替换成元素e
    def replace(self,e):
        re = self.__data[self.__indexs[0]]
        self.__data[self.__indexs[0]] = e
        self.__slipDown(0)
        return re

    def __getitem__(self, item):
        return self.__data[item]

    def __str__(self):
        re = '['
        for i in self.__indexs:
            re += str(self.__data[i])+', '

        re = re[: -2] + ']'
        return re

if __name__ == '__main__':
    arr = [41, 62, 28, 30, 16, 13, 19, 17, 15, 22]
    maxheap = MaxIndexHeap()
    # for i in range(len(arr)):
    #     maxheap.add(i, arr[i])
    # print(maxheap)
    # re = maxheap.extraMax()
    # maxheap.change1(3,66)
    # pass

    print(maxheap.heapify([41, 62, 28, 30, 16, 13, 19, 17, 15, 22]))
    maxheap.replace(10)
    print(maxheap)
    print(maxheap[0])

