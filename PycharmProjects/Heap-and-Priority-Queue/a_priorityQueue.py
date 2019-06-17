from a_maxHeap import MaxHeap

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






