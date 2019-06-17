from dummyhead import LinkedList

class dumLinkedStack():
    def __init__(self):
        self.__data = LinkedList()

    def getSize(self):
        return self.__data.getSize()

    def isEmpty(self):
        return self.__data.isEmpty()

    def push(self,e):
        self.__data.addFirst(e)

    def pop(self):
        return self.__data.removeFirst()

    def peek(self):
        return self.__data.getFirst()

    def __str__(self):
        res = 'Stack: top '
        res += str(self.__data)
        return res

if __name__ == '__main__':
    mystack = dumLinkedStack()
    for i in range(5):
        mystack.push(i)
    print(mystack)

    print(mystack.pop())
    print(mystack)