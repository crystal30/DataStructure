class LinkedList:

    class Node:
        def __init__(self,e=None,next=None):
            self.e = e
            self.next = next
        def __repr__(self):
            return str(self.e)


    def __init__(self):
        self.__dummyhead = self.Node()
        self.__size = 0

    # 获取链表中元素的个数：
    def getSize(self):
        return self.__size

    #返回链表是否为空
    def isEmpty(self):
        return self.__size == 0


    # 在链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用：）

    def add(self, index, e):

        assert index >= 0 and index <= self.__size, "index is invalid"

        prev = self.__dummyhead
        for i in range(index):
            prev = prev.next
        prev.next = self.Node(e, prev.next)
        self.__size += 1

    # 在链表头添加新的元素e
    def addFirst(self, e):
        self.add(0, e)

    # 在链表的末尾添加元素e
    def addLast(self, e):
        self.add(self.__size, e)

    # 获得链表的第index(0 - based)个位置的元素
    # 在链表中不是一个常用的操作，练习用：）
    def get(self, index):
        assert index >= 0 and index <= self.__size, "index is invalid"
        cur = self.__dummyhead.next
        for i in range(index):
            cur = cur.next
        return cur.e

    def getFirst(self):
        return self.get(0)


    def getLast(self):
        return self.get(self.__size-1)

    # 修改链表的第index(0 - based)个位置的元素为e
    # 在链表中不是一个常用的操作，练习用：）
    def set(self, index, e):
        assert index >= 0 and index <= self.__size, "index is invalid"
        cur = self.__dummyhead.next
        for i in range(index):
            cur = cur.next
        cur.e = e

    #查找链表中是否有元素e
    def contains(self, e):
        cur = self.__dummyhead.next
        while(cur != None):
            if cur.e == e:
                return True
            else:
                cur = cur.next
        return False

    # 从链表中删除index(0 - based)位置的元素, 返回删除的元素
    # 在链表中不是一个常用的操作，练习用：）
    def remove(self,index):
        assert index >= 0 and index <= self.__size, "index is invalid"
        prev = self.__dummyhead
        for i in range(index):
            prev = prev.next

        retNode = prev.next
        prev.next = retNode.next
        retNode.next = None
        self.__size -= 1
        return retNode.e

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
    link = LinkedList()
    link.addFirst(0)
    print(link)
    link.addFirst(1)
    print(link)
    link.addFirst(2)
    print(link)
    link.add(2,666)
    print(link)
    link.addLast(999)
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
    print(link.removeLast())
    print(link)
