from myarray import Array

class ArrayQueue:
    def __init__(self,capacity=10):
        self.__myqueue = Array(capacity)

    def getSize(self):
        return self.__myqueue.getSize()

    def isEmpty(self):
        return self.__myqueue.isEmpty()

    def enqueue(self,e):
        self.__myqueue.addLast(e)

    def dequeue(self):
        return self.__myqueue.removeFirst()

    def getFront(self):
        return self.__myqueue.getFirst()

    def __str__(self):
        res = 'front:['
        for i in range(self.__myqueue.getSize()):
            res += str(self.__myqueue.get(i))
            if i != self.__myqueue.getSize() - 1:
                res += ', '
        res += '] tail'
        return res

if __name__ == '__main__':
    myq = ArrayQueue(capacity=5)
    print(myq.getSize())
    print(myq.isEmpty())
    # print(myq.dequeue())
    # print(myq.getFront())
    for i in range(3):
        myq.enqueue(i)
    print(myq)
    myq.enqueue(9)
    print(myq)
    print(myq.getSize())
    print(myq.isEmpty())
    print(myq.dequeue())
    print(myq.getFront())

