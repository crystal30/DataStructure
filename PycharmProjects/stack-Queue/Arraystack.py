#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from myarray import Array
class ArrayStack():

    def __init__(self,capacity=10):
        self.__array = Array(capacity)

    def getSize(self):
        return self.__array.getSize()

    def isEmpty(self):
        return self.__array.isEmpty()

    def getCapacity(self):
        return self.__array.getCapacity()

    def push(self,e):
        return self.__array.addLast(e)

    def pop(self):
        return self.__array.removeLast()

    def peek(self):
        return self.__array.getLast()

    def __str__(self):
        res = 'ArrayStack: size = %d, capacity = %d\n' %(self.getSize(), self.getCapacity())
        res += '['
        for i in range(self.getSize()):
            res += str(self.__array.get(i))
            if i != self.getSize()- 1:
                res += ', '
        res += '] top'
        return res

if __name__ == '__main__':

    arrStack = ArrayStack(10)
    print(arrStack.getSize())
    print(arrStack.getCapacity())
    print(arrStack.isEmpty())

    for i in range(10):
        arrStack.push(i)

    print(arrStack.getSize())
    print(arrStack.getCapacity())
    print(arrStack.isEmpty())
    print(arrStack)

    print(arrStack.pop())
    print(arrStack)

    print(arrStack.peek())


