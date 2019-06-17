
class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    #让其不添加进重复的元素
    def add(self,e):
        self.arr.append(e)
        self.size += 1
        self.__shiftUp(self.size -1)

    #再看一下这个函数，到底应该怎么写
    def __shiftUp(self,i):
        p = (i - 1) // 2
        while p >= 0:
            if self.arr[i] < self.arr[p]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                p = (p - 1) // 2
            else:
                break
    def extractMin(self):
        re = self.arr[0]
        i = self.getSize()-1
        self.arr[0] = self.arr[i]
        self.arr.pop()
        self.size -= 1
        self.__shiftDown(0)
        return re

    def __shiftDown(self,i):
        j = i * 2 + 1  # j用来存放 左右子节点中最小的那个节点的下标
        # 递归结束的条件
        if j >= self.size:
            return
        #当j < self.size
        if j + 1 < self.size:
            if self.arr[j + 1] < self.arr[j]:
                j = j + 1
        if self.arr[i] > self.arr[j]:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.__shiftDown(j)


