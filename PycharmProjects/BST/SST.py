#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node():
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next
#这里SST（sequence search table）是一个无序的链表
class SST:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, key, value):
        cur = self.head
        #初始的cur为链表的头节点
        while cur is not None:
            if key == cur.key:
                cur.value = value
                return
            else:
                cur = cur.next

        #当cur为空时,创建新的节点，将该节点加在链表的头部（因为我们定义了头部的指针，所以在头部加节点更方便）
        # newNode = Node(key, value)
        # newNode.next = self.head
        # self.head = newNode
        self.head = Node(key, value, self.head) #等价于上边的三句
        self.size += 1

    #查找链表中是否存在 元素key，存在返回true，不存在返回False
    def cotains(self, key):
        cur = self.head
        while cur != None:
            if key == cur.key:
                return True
            else:
                cur = cur.next
        #遍历完毕，即到cur == None 时，仍未找到与key相等的元素，说明该链表中不存在该元素，返回false
        return False

    #查找链表中元素为key的值value， 若链表中存在key，返回相应的value值，若不存在key，返回None
    def search(self, key):
        cur = self.head
        while cur != None:
            if key == cur.key:
                return cur.value
            else:
                cur = cur.next
        # 遍历完毕，即到cur == None 时，仍未找到与key相等的元素，说明该链表中不存在该元素，返回None
        return None

#这里的SST1（sequence search table）本质是顺序链表，这里的key需要是可以比较的对象
#在顺序链表中，是以每个元素的key的大小从小到大排序的
class SST1:
    def __init__(self):
        self.dummyhead = Node()
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def insert(self, key, value):
        prev = self.dummyhead
        while prev.next is not None:
            if key == prev.next.key:
                prev.next.value = value
                return

            elif key > prev.next.key:
                prev = prev.next

            else:# key < prev.next.key
                # newNode = Node(key, value)
                # newNode.next = prev.next
                # prev.next = newNode
                prev.next = Node(key, value, prev.next)
                return

        #当prev.next为空时，创建新的节点，目前想到的两种情况（1，当链表为空时，2，当key比链表的最大元素还要大时）
        prev.next = Node(key, value, prev.next)

    #在顺序链表中查找 是否寻在元素key，存在返回True， 不存在返回False
    def contains(self, key):
        prev = self.dummyhead
        while prev.next != None:
            if key == prev.next.key:
                return True
            elif key > prev.next.key:
                prev = prev.next
            else:
                return False
        #当遍历完了，还未找到key，说明该链表中不存在key（目前想到的两种情况（1，当链表为空时，2，当key比链表的最大元素还要大时））
        return False

    #在顺序链表中查找 是否存在元素key，存在返回相对应的value值， 若不存在返回None
    def search(self, key):
        prev = self.dummyhead
        while prev.next != None:
            if key == prev.next.key:
                return prev.next.value
            elif key > prev.next.key:
                prev = prev.next
            else: # key< prev.next
            #在这里分两种情况，一种时要查找的key比头节点（不是dummyhead）还要小，
            # 由于时顺序链表，所以该元素肯定不在该链表中，直接返回None
            #另一种是 当key大于前一个节点的key， 但却小于后一个节点的key，由于链表是有序的，此时即可断定key不在该元素中
                return None
        #当遍历完了，还未找到key，说明该链表中不存在key（目前想到的两种情况（1，当链表为空时，2，当key比链表的最大元素还要大时））
        return None












