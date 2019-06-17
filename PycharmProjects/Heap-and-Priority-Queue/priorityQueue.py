from maxHeap1 import MaxHeap

class PriorityQueue():
    def __init__(self):
        self.maxHeap = MaxHeap()

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
