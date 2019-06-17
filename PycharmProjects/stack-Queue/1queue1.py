class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def getSize(self):
        return len(self.item)

    # 将索引为0的元素看作队首
    def enqueue(self, e):
        self.item.append(e)

    def getFront(self):
        return self.item[0]

    def dequeue(self):
        return self.item.pop(0)

    def __str__(self):
        return str(self.item)

if __name__ == '__main__':
    myq = Queue()
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