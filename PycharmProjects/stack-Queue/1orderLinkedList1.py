class Node():
    def __init__(self, e=None, next=None):
        self.e = e
        self.next = next
    def __str__(self):
        return str(self.e)

class OrderLinkedList():
    def __init__(self):
        self.__dummyhead = Node()
        self.__size = 0

    def getSize(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    # 假设该有序链表是 从小到大排列的
    def add(self, e):
        prev = self.__dummyhead
        while prev.next != None and prev.next.e < e:
            prev = prev.next

        newNode = Node(e, prev.next)
        prev.next = newNode
        self.__size += 1


    def contains(self,e):
        prev = self.__dummyhead
        while prev.next!= None and prev.next.e < e:
            prev = prev.next
            if prev.next == e:
                return True
            else: # prev.next.e > e:
                return False
        return False

    def get(self, index):
        prev = self.__dummyhead
        for i in range(index):
            prev = prev.next
        return prev.next.e

    def getFirst(self):
        return self.get(0)

    def getLast(self):
        return self.get(self.__size-1)

    def set(self, index, e):
        prev = self.__dummyhead
        for i in range(index):
            prev = prev.next
        prev.next.e = e

    def remove(self,index):
        prev = self.__dummyhead
        for i in range(index):
            prev = prev.next
        cur = prev.next
        re = cur.e
        prev.next = cur.next
        cur.next = None
        self.__size -= 1

        return re

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self.__size-1)

    def __str__(self):
        cur = self.__dummyhead.next
        res = ''
        while (cur is not None):
            res += str(cur.e) + '-->'
            cur = cur.next
        res += 'None'
        return res

if __name__ == '__main__':
    link = OrderLinkedList()
    link.add(0)
    print(link)
    link.add(1)
    print(link)
    link.add(2)
    print(link)
    link.add(666)
    print(link.getSize())
    print(link)
    link.add(999)
    print(link)
    link.set(3, 8)
    print(link)
    print(link.get(3))
    print(link.getFirst())
    print(link.getLast())
    print(link.contains(666))
    print(link.contains(6))

    print('link.remove')
    print(link.remove(2))
    print(link)
    print(link.removeFirst())
    print(link)
    print(link.getSize())
    print(link.removeLast())
    print(link)








