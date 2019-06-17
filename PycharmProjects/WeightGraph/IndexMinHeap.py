class IndexMinHeap:
    def __init__(self,capacity):
        self.indexs = [_ for _ in range(capacity)]  #存储元素下标，在构造堆时，时该索引改变，而self.data不改
        self.data = [float('inf')]*capacity
        self.size = capacity

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    #从最小堆的第i个位置开始下沉
    def __shiftDown(self, i):

        j = 2*i + 1 #j用来表示arr[i]左右孩子中最小的元素的下标，此时 2*i+1为i的左孩子
        #递归结束的条件
        if j >= len(self.indexs):
            return

        #当j<len(arr)时
        if j+1 < len(self.indexs):
            if self.data[self.indexs[j+1]] < self.data[self.indexs[j]]:
                j = j+1
        if self.data[self.indexs[i]] > self.data[self.indexs[j]]:
            self.indexs[i], self.indexs[j] = self.indexs[j], self.indexs[i]
            self.__shiftDown(j)

    # 从最小堆的第i个位置开始上浮（位置是从0开始的）
    def __shiftUp(self, i):

        p = (i-1)//2 #p为节点i的父节点，由于是最小堆，所以父节点肯定要比孩子节点小
        #递归结束的条件
        if p < 0:
            return
        #当p>=0时，即存在父节点
        if self.data[self.indexs[p]] > self.data[self.indexs[i]]:
            self.indexs[p], self.indexs[i] = self.indexs[i], self.indexs[p]
            self.__shiftUp(p)

    def extraMin(self):
        re = self.indexs[0]
        self.indexs[0] = self.indexs.pop()
        self.size -= 1
        self.__shiftDown(0)
        return re

    #当self.arr[i]的位置的元素发生改变时(即变为新的值newe时)，需要shiftUp 和ShiftDown
    def change(self, i,newe):
        self.data[i] = newe
        self.__shiftDown(self.indexs.index(i))
        self.__shiftUp(self.indexs.index(i))

if __name__ == '__main__':
    arr = [float('inf')]*10
    im = IndexMinHeap()
    im.heapify(arr)
    im.change(3,0)
    im.extraMin()
    pass
