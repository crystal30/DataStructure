#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class BSTmap:
    class __Node():
        def __init__(self,key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0

    # 添加元素2
    def add(self,key, value):
        self.root = self.__add(self.root, key, value)

    # 返回新插入节点后，二分搜索树的根
    def __add(self,Node, key, value):
        if Node is None:
            self.size += 1
            return self.__Node(key,value)

        if Node.key > key:
            Node.left = self.__add(Node.left, key, value)
        elif Node.key < key:
            Node.right = self.__add(Node.right, key, value)
        return Node

    def __getNode(self, Node, key):
        if Node == None:
            return None
        else:
            if Node.key == key:
                return Node
            elif Node.key > key:
                return self.__getNode(Node.left, key)
            else:
                return self.__getNode(Node.right, key)
    def contains(self, key):
        return False if self.__getNode(self.root, key) is None else True

    def get(self,key):
        cur = self.__getNode(self.root, key)
        return None if cur is None else cur.value

    def set(self, key, newvalue):
        cur = self.__getNode(self.root, key)
        assert cur is not None, "The map must contain this key"
        cur.value = newvalue

    def remove(self,key):
        cur = self.__getNode(self.root, key)
        if cur is None:
            return None
        else:
            self.root = self.__remove(self.root, key)
        return cur.value

    # 返回删除某个元素后，此子树的根
    def __remove(self, Node, key):
        if Node == None:
            return None

        if Node.key > key:
            Node.left = self.__remove(Node.left, key)
            return Node

        elif Node.key < key:
            Node.right = self.__remove(Node.right, key)
            return Node
        else:
            if Node.right == None:
                leftNode = Node.left
                Node.left = None
                self.size -= 1
                return leftNode

            if Node.left == None:
                rightNode = Node.right
                Node.right = None
                self.size -= 1
                return rightNode

            elif Node.left != None and Node.right != None:
                minNode = self.__minimum(Node.right)
                minNode.right = self.__removeMin(Node)
                minNode.left = Node.left
                Node.left, Node.right = None, None
                return minNode


    # 返回以node为根的二分搜索树的最小值所在的节点
    def __minimum(self,Node):

        if Node.left == None:
            return Node

        return self.__minimum(Node.left)

    #删除掉以node为根的二分搜索树中的最小节点
    #返回删除节点后新的二分搜索树的根
    def __removeMin(self,Node):
        if Node.left == None:
            rightNode = Node.right
            self.size -= 1
            return rightNode
        Node.left = self.__removeMin(Node.left)
        return Node

if __name__ == '__main__':
    link = BSTmap()
    words = ['12','12','34','56','56','12']
    for word in words:
        if link.contains(word):
            link.set(word, link.get(word)+1)
        else:
            link.add(word,1)
    print(link.get('12'))
    print(link.get('34'))
    print(link.remove('56'))
    print(link.getSize())








