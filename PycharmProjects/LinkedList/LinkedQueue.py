# -*- coding: utf-8 -*-

class LinkedQueue:

    class Node:
        def __init__(self,e=None,next=None):
            self.e = e
            self.next = next
        def __repr__(self):
            return str(self.e)

        # def __str__(self):
        #     return str(self.e)


    def __init__(self):

        self.__head = None
        self.__tail = None
        self.__size = 0

    # 获取链表中元素的个数：
    def getSize(self):
        return self.__size

    #返回链表是否为空
    def isEmpty(self):
        return self.__size == 0

    def enqueue(self,e):

        if self.isEmpty():
            self.__tail = self.Node(e)
            self.__head = self.__tail
        else:
            self.__tail.next = self.Node(e)
            self.__tail = self.__tail.next

        self.__size += 1

    def dequeue(self):
        assert self.__size != 0, "queue must not be Empty"

        rehead = self.__head
        self.__head = self.__head.next
        rehead.next = None

        if self.__head == None:
            self.__tail = None
        self.__size -= 1
        return rehead.e

    def getFront(self):
        assert self.__size != 0, "queue must not be Empty"
        return self.__head.e


    def __str__(self):
        cur = self.__head
        res = ''
        while (cur is not None):
        # for i in range(self.__size):
            res += str(cur.e) + '-->'
            cur = cur.next

        res += 'None'
        return res


if __name__ == '__main__':
    linkq = LinkedQueue()
    linkq.getSize()
    linkq.isEmpty()

    for i in range(5):
        linkq.enqueue(i)
    print(linkq)

    print(linkq.dequeue())
    print(linkq)