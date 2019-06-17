#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Array(object):

    # 构造函数，传入数组的容量capacity构造array
    # 无参数的构造函数，默认数组的容量capacity=10
    def __init__(self,capacity = 10):
        self.__data = [None]*capacity
        self.__size = 0

    # 获取数组中元素的个数
    def getSize(self):
        return self.__size

    # 获取数组的容量
    def getCapacity(self):
        return len(self.__data)

    # 返回数组是否为空
    def isEmpty(self):
        return self.__size == 0

    #向所有元素后添加一个新元素
    # def addLast(self, e):
    #     assert self.__size < len(self.__data), "addLast is failed. Array is full"
    #     self.__data[self.__size] = e
    #     self.__size += 1

    # 向所有元素后添加一个新元素 也可以调用add方法
    def addLast(self, e):
        self.add(self.__size, e)

    #同理，也可以调用add 向数组的开始添加一个元素
    def addFirst(self, e):
        self.add(0, e)

    #向指定的位置添加元素
    def add(self, index, e):
        #assert self.__size < len(self.__data), "add is failed. Array is full"
        assert (index >= 0) and (index <= len(self.__data)), \
            "add is failed. Required index >= 0 and index <= size"
        # 动态数组，如果self.__size == len(self.__data) 扩容为原来数组的两倍
        if self.__size == len(self.__data):
            self.__resize(len(self.__data)*2)

        i = self.__size - 1
        while i >= index:
            self.__data[i+1] = self.__data[i]
            i -= 1
        self.__data[index] = e
        self.__size += 1

    #获取index索引位置的元素
    def get(self, index):
        assert (index >= 0) and (index < self.__size), "Get failed, index is Illegal."
        return self.__data[index]

    def getFirst(self):
        return self.get(0)


    def getLast(self):
        return self.get(self.__size-1)

    #修改index索引位置的元素为e
    def set(self, index, e):
        assert (index >= 0) and (index < self.__size), "Get failed, index is Illegal."
        self.__data[index] = e

    #查找数组中是否存在元素e
    def contains(self, e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return True
        return False
    #查找数组中是否存在e，若存在，返回存在的个数，若不存在返回0
    def containsCount(self, e):
        count = 0
        for i in range(self.__size):
            if self.__data[i] == e:
                count += 1
        return count

    #查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    def find(self, e):
        for i in range(self.__size):
            if self.__data[i] == e:
                return i
        return -1

    #查找数组中元素e所在的位置的所有索引（数组中可能包含多个e），若不存在元素e，返回-1
    def findAll(self, e):
        indexs = []
        for i in range(self.__size):
            if self.__data[i] == e:
                indexs.append(i)
        if len(indexs) == 0:
            return -1
        else:
            return indexs


    #从数组中删除index位置的元素，返回被删除的元素
    def remove(self, index):
        assert (index >= 0) and (index < self.__size), "remove failed, index is illegal"
        # if self.__size <= len(self.__data)/2:
        # lazy ,优化时间复杂度
        if self.__size <= len(self.__data)/4:
            self.__resize(int(len(self.__data)/2))
        ret = self.__data[index]
        for i in range(index, self.__size - 1):
            self.__data[i] = self.__data[i+1]
        self.__size -= 1
        return ret

    #删除第一个元素
    def removeFirst(self):
        return self.remove(0)

    #删除最后一个元素
    def removeLast(self):
        return self.remove(self.__size - 1)

    #若数组中含有元素e,则删除一个
    def removeElement(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    #若数组中含有元素e，删除掉所有的元素e
    def removeAllElement(self, e):
        indexs = self.findAll(e)
        temp = 0
        if indexs != -1:
            for i in indexs:
                self.remove(i-temp)
                temp += 1

    def __resize(self, newCapacity):
        newarr = [None] * newCapacity
        for i in range(self.__size):
            newarr[i] = self.__data[i]
        self.__data = newarr

    def __str__(self):
        res = 'Array: size = %d, capacity = %d\n' %(self.__size, len(self.__data))
        res += '['
        for i in range(self.__size):
            res += str(self.__data[i])
            if i != self.__size - 1:
                res += ', '
        res += ']'
        return res

if __name__ == '__main__':
    arr = Array(10)
    for i in range(10):
        arr.addLast(i)
    print(arr)
    arr.addFirst(5)
    arr.addFirst(6)
    arr.addFirst(5)
    print(arr)

    arr.remove(6)
    print("remove the index 6 element)")
    print(arr)
    arr.removeElement(6)
    print("remove elememt 6")
    print(arr)
    arr.removeAllElement(5)
    print("remove allElement 5")
    print(arr)
    arr.removeFirst()
    print("remove first")
    print(arr)
    arr.removeLast()
    print("remove last")
    print(arr)

    arr.removeLast()
    print("remove last")
    print(arr)

    arr.removeLast()
    print("remove last")
    print(arr)

    arr.set(3, 666)
    print("arr.set(3, 666)")
    print(arr)

