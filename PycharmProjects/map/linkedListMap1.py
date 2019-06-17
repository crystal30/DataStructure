# -*- coding: utf-8 -*-

class LinkedListMap:

    class Node:
        def __init__(self,key=None,value=None, next=None):
            self.key = key
            self.value = value
            self.next = next
        def __repr__(self):
            return str(self.key)


    def __init__(self):

        self.__dummyHead = self.Node()
        self.__size = 0

    # 获取链表中元素的个数：
    def getSize(self):
        return self.__size

    #返回链表是否为空
    def isEmpty(self):
        return self.__size == 0

    def __getNode(self,key):
        cur = self.__dummyHead.next
        while cur is not None:
            if cur.key != key:
                cur = cur.next
                continue
            else:
                return cur
        return None

    #查找元素
    def contains(self,key):
        return False if self.__getNode(key) == None else True

    def get(self,key):
        cur = self.__getNode(key)
        return None if cur == None else cur.value

    #在链表头添加新的元素e
    def add(self,key,value):
        cur = self.__getNode(key)
        if cur is None:
            # node = self.Node(key, value)
            # node.next = self.__dummyHead.next
            # self.__dummyHead.next = node

            self.__dummyHead.next = self.Node(key, value, self.__dummyHead.next)
            self.__size += 1
        else:
            cur.value = value

    def set(self, key, newvalue):
        cur = self.__getNode(key)
        assert cur is not None, "the map must contain key"
        cur.value = newvalue


    #删除元素
    def remove(self,key):
        prev = self.__dummyHead
        while prev.next is not None:
            while prev.next.key == key:
                re = prev.next.value
                prev.next = prev.next.next
                self.__size -= 1
                return re
            prev = prev.next
        return None


    def __str__(self):
        cur = self.__dummyHead.next
        res = '{'
        while (cur is not None):
        # for i in range(self.__size):
            res += str(cur.key) +':'+str(cur.value)+', '
            cur = cur.next
        res =res[:-2]+ '}'
        return res


if __name__ == '__main__':
    link = LinkedListMap()
    words = ['12','12','34','56','56','12']
    for word in words:
        if link.contains(word):
            link.set(word, link.get(word)+1)
        else:
            link.add(word,1)
    print(link)

