# -*- coding: utf-8 -*-

class LinkedListMap:

    class Node:
        def __init__(self,key=None,value=None, next=None):
            self.key = key
            self.value = value
            self.next = next
        # def __str__(self):
        #     return str(self.key)+":"+str(self.value)


    def __init__(self):

        self.__head = self.Node()
        self.__size = 0

    # 获取链表中元素的个数：
    def getSize(self):
        return self.__size

    #返回链表是否为空
    def isEmpty(self):
        return self.__size == 0

    #查找元素
    def contains(self,key):
        cur = self.__head
        while cur.key is not None:
            if cur.key != key:
                cur = cur.next
                continue
            else:
                return True
        return False

    def get(self,key):
        cur = self.__head
        while cur.key is not None:
            if cur.key != key:
                cur = cur.next
                continue
            else:
                return cur.value
        return None

    #在链表头添加新的元素e

    def addFirst(self,key,value):
        node = self.Node(key, value)
        node.next = self.__head
        self.__head = node

        #self.__head = self.Node(e, self.__head)
        self.__size += 1

    #删除元素，当含有return时，如果该链表中有两个e, 则只删除第一个e； 当不含return时，不管有所少个e都会被删除
    def remove(self,key):
        prev = self.__head
        #当头节点就是要删除的元素时
        while prev is not None:
            if prev.key == key:
                re = prev.value
                prev = prev.next
                self.__head = prev
                return re
            else:
                break
        #当头节点不是要删除的节点
        while prev.next is not None:
            while prev.next.key == key:
                re = prev.next.value
                prev.next = prev.next.next
                return re
            prev = prev.next



    def __str__(self):
        cur = self.__head
        res = '{'
        while (cur.key is not None):
        # for i in range(self.__size):
            res += str(cur.key) +':'+str(cur.value)+','
            cur = cur.next
        res += '}'
        return res


if __name__ == '__main__':
    link = LinkedListMap()
    link.addFirst(0,'zero')
    link.addFirst(1,'one')
    link.addFirst(2, 'two')
    link.addFirst(2, 'two')
    print(link)

    print(link.getSize())
    print(link.isEmpty())
    print(link.get(2))

    print(link.contains(999))
    print(link.remove(999))
    print(link)
    print(link.remove(2))
    print(link)

    link.addFirst(666,'six,six,six')
    print(link)
    print(link.remove(666))
    print(link)

