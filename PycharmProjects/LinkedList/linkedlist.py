# -*- coding: utf-8 -*-

class LinkedList:

    class Node:
        def __init__(self,e=None,next=None):
            self.e = e
            self.next = next
        def __repr__(self):
            return str(self.e)

        # def __str__(self):
        #     return str(self.e)


    def __init__(self):

        self.__head = self.Node()
        self.__size = 0

    # 获取链表中元素的个数：
    def getSize(self):
        return self.__size

    #返回链表是否为空
    def isEmpty(self):
        return self.__size == 0

    #在链表头添加新的元素e

    def addFirst(self,e):
        node = self.Node(e)
        node.next = self.__head
        self.__head = node

        #self.__head = self.Node(e, self.__head)
        self.__size += 1

    # 在链表的index(0-based)位置添加新的元素e
    # 在链表中不是一个常用的操作，练习用：）

    def add(self, index, e):

        assert index >= 0 and index <= self.__size, "index is invalid"

        if index == 0:
            self.addFirst(e)
        else:
            prev = self.__head
            for i in range(index):
                prev = prev.next

            # node = self.Node(e)
            # node.next = prev.next
            # prev.next = node

            prev.next = self.Node(e, prev.next)

        self.__size += 1

    # 在链表的末尾添加元素e
    def addLast(self, e):
        self.add(self.__size-1, e)

    def __str__(self):
        cur = self.__head
        res = ''
        while (cur.e is not None):
        # for i in range(self.__size):
            res += str(cur.e) + '-->'
            cur = cur.next

        res += 'None'
        return res


if __name__ == '__main__':
    link = LinkedList()
    link.addFirst(0)
    link.addFirst(1)
    link.addFirst(2)
    link.add(2,666)
    link.addLast(999)

    print(link)
