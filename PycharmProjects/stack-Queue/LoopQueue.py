class LoopQueue:

    def __init__(self,capacity=10):
        self.__font = 0
        self.__tail = 0
        self.__size = 0
        self.__data = [None] *(capacity+1)


    def getCapacity(self):
        return len(self.__data)-1

    def isEmpty(self):
        return self.__font == self.__tail

    def getSize(self):
        return self.__size

    def enqueue(self,e):

        c = self.getCapacity()
        if self.__size == c:
            self.__data = self.resize(c*2)

        self.__data[self.__tail] = e
        self.__tail = (self.__tail + 1) % (self.getCapacity()+1)
        self.__size +=1

    def dequeue(self):
        assert self.isEmpty() != True, "This Queue must not be empty."

        re = self.__data[self.__font]
        self.__data[self.__font] = None
        self.__font = (self.__font + 1) % (self.getCapacity()+1)
        self.__size -= 1

        if self.__size == int(self.getCapacity()/ 4) and int(self.getCapacity()/2) != 0:
            self.__data = self.resize(int(self.getCapacity()/2))

        return re

    def getFront(self):
        assert self.isEmpty() != True, "This Queue must not be empty."
        return self.__data[self.__font]

    def resize(self,new_capacity):
        new_que = [None] * (new_capacity+1)
        c = self.getCapacity()
        for i in range(self.__size):
            new_que[i] = self.__data[(self.__font + i) % (c + 1)]
        self.__data = new_que
        self.__font = 0
        self.__tail = self.__size

        return self.__data

    def __str__(self):

        res = 'Queue: size = {0} , capacity = {1}\n'.format( self.__size, self.getCapacity());
        res += 'front:['
        for i in range(self.__size):
            res += str(self.__data[(self.__font + i) % (self.getCapacity() + 1)])
            if i != self.__size -1:
                res += ', '
        res += '] tail'
        return res

if __name__ == '__main__':
    myq = LoopQueue(capacity=5)
    print(myq.getSize())
    print(myq.isEmpty())
    for i in range(5):
        myq.enqueue(i)
    print(myq)
    myq.enqueue(9)
    print(myq)
    print(myq.getSize())
    print(myq.isEmpty())
    print(myq.dequeue())
    print(myq.dequeue())
    print(myq.dequeue())
    print(myq.dequeue())
    print(myq)
    myq.enqueue(6)
    myq.enqueue(9)
    myq.enqueue(12)
    print(myq)
    print(myq.getFront())
    print(myq)


