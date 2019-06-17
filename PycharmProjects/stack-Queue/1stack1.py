class Stack():
    def __init__(self):
        self.item = []

    def getSize(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []

    #把列表的最后一个元素当作栈顶
    def peek(self):
        return self.item[-1]

    def pop(self):
        return self.item.pop()

    def push(self,e):
        return self.item.append(e)

    def __str__(self):
        return str(self.item) + 'peek'

if __name__ == '__main__':

    arrStack = Stack()
    print(arrStack.getSize())
    print(arrStack.isEmpty())

    for i in range(10):
        arrStack.push(i)

    print(arrStack.getSize())
    print(arrStack.isEmpty())
    print(arrStack)

    print(arrStack.pop())
    print(arrStack)

    print(arrStack.peek())


