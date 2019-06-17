#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
class Node():
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return self.key

class BST():
    def __init__(self):
        self.root = None
        self.size = 0

    #查询该BST是否为空
    def isEmpty(self):
        return self.size == 0

    #返回BST中元素的个数
    def getSize(self):
        return self.size

    #插入元素
    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    #从某个节点开始插入元素，并返回此节点
    def __insert(self, node, key, value):

        if node == None:
            self.size += 1
            return Node(key, value)
        if key < node.key:
            node.left = self.__insert(node.left, key, value)
        elif key > node.key:
            node.right = self.__insert(node.right, key, value)
        else:# key == node.key
            node.value = value
        return node

    #查询 二分搜索树中是否包含某个元素key，包含返回True， 不包含返回False
    def contains(self, key):
        return self.__contains(self.root, key)

    #从某个节点为跟节点，查询，其是否包含某个元素key, 包含返回True，不包含返回False
    def __contains(self, node, key):
        if node.key == None:
            return False

        if key < node.key:
            return self.__contains(node.left, key)
        elif key > node.key:
            return self.__contains(node.right, key)
        else: # key == node.key
            return True

    #查寻某一个元素是否在二分搜索树中，若存在，返回value值
    #若不存在返回None
    #实现方法与contains 类似
    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        if node == None:
            return None
        if key < node.key:
            return self.__search(node.left, key)
        elif key > node.key:
            return self.__search(node.right, key)
        else:#key == node.key
            return node.value

    # 删除BST中的最小元素
    # 首先，BST中的最小节点不可能有左子树,可分为两种情况：1。没有右子树，2。有右子树

    def removemin(self):
        self.root = self.__removemin(self.root)

    # 删除以node为根节点的树中最小的元素，并返回删除最小元素后的跟节点
    def __removemin(self, node):
        if node == None:
            return None

        if node.left == None:
            # 当node.left == None 时，即该节点就是最小节点
            return node.right if node.right != None else None
        else: # node.left != None 即当前的节点还不是 最小节点
            node.left = self.__removemin(node.left)
        return node

    #返回BST中的最大元素
    def minimium(self):
        minNode = self.__min(self.root)
        return minNode.key

    #返回BST中的最大元素
    def maximium(self):
        maxNode = self.__max(self.root)
        return maxNode.key

    #删除BST中的最大元素
    #首先，BST中的最大节点不可能有右子树,可分为两种情况：1。没有左子树，2。有左子树
    def removemax(self):
        self.root = self.__removemax(self.root)

    #删除以node为根节点的树中最大的元素，并返回删除最大元素后的跟节点
    def __removemax(self, node):
        if node == None:
            return None

        if node.right == None:
            #当node.right == None 时，即该节点就是最大节点
            return node.left if node.left != None else None
        else:
            node.right = self.__removemax(node.right)

        return node

    #删除BST中的最小元素

    #删除任意一个元素
    # 注意：删除的元素必须在该BST中
    def remove(self, key):
        assert self.contains(key), "key is not in BST"
        self.root = self.__remove(self.root, key)

    #从以node为根节点的树中删除某个元素, 并返回跟节点
    def __remove(self, node, key):
        if node == None:
            return None

        #node != None
        if key < node.key:
            node.left = self.__remove(node.left, key)
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        else: #node.key = key 即node 就是要删除的节点
            if node.right == None:
            #在此种情况下，包括 node.right == None and node.left == None；
            # node.right == None and node.left ！= None 两种情况
                renode = node.left
                self.size -= 1
            elif node.left == None:
                #由于是if， elif语句，只有当node.left == None and node.right ！= None时才会进入这个语句
                renode = node.right
                self.size -= 1
            #要删除的节点左子树和右子树都不为空
            #方法一：找出右子树中最小的节点，来代替现有要删除的节点（示例采用此种方法）
            #方法二：找出左子树中最大的节点，来代替现有要删除的节点
            elif node.left != None and node.right != None:
                renode = self.__min(node)
                #注意要在以node为跟的树中删除掉 minNode
                renode.right = self.__removemin(node)
                renode.left = node.left
                self.size -= 1
            return renode
        return node


    #从以node为跟节点的树中，找到最小的节点，并返回该节点
    def __min(self, node):
        if node == None:
            return None

        #node != None
        #由于是要在BST中寻找最小元素，所以只要左子树为空，最小元素肯定是该节点（节点的左子树都小于该节点，右子树都大于该节点）
        if node.left == None:
            return node

        #由于是要在BST中寻找最小元素，所以只要有左子树，最小元素肯定是在左子树中的
        else:# node.left != None:
            return self.__min(node.left)

    # 从以node为跟节点的树中，找到最小的节点，并返回该节点
    def __max(self, node):
        if node == None:
            return None

        # node != None
        # 由于是要在BST中寻找最大元素，所以只要右子树为空，最大元素肯定是该节点（节点的左子树都小于该节点，右子树都大于该节点）
        if node.right == None:
            return node

        # 由于是要在BST中寻找最小元素，所以只要有左子树，最小元素肯定是在左子树中的
        else:  # node.right != None:
            return self.__min(node.right)


    #前序遍历
    def preOrder(self):
        self.__preOrder(self.root)

    def __preOrder(self, node):
        if node == None:
            return
        #此时，当Node != None
        print(node.key)
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    #中序遍历
    def inOrder(self):
        self.__inOrder(self.root)

    def __inOrder(self, node):
        if node == None:
            return
        #此时，当node ！= None
        self.__inOrder(node.left)
        print(node.key)
        self.__inOrder(node.right)

    # 后序遍历
    def postOrder(self):
        self.__postOrder(self.root)

    def __postOrder(self, node):
        if node == None:
            return
        #此时，当node != None
        self.__postOrder(node.left)
        self.__postOrder(node.right)
        print(node.key)
    #层序优先遍历
    #思路，将节点推入队列中，出队时，将该节点的左右两个孩子依次推入队列
    def SequenceOrder(self):
        myqueue = []
        if self.root == None:
            return
        # self.root != None
        myqueue.append(self.root)
        while len(myqueue) != 0:
            cur = myqueue.pop(0)
            print(cur.key)
            if cur.left != None:
                myqueue.append(cur.left)
            if cur.right != None:
                myqueue.append(cur.right)

# 词频统计
if __name__ == '__main__':
    bst = BST()
    for key in [5, 3, 6, 8,4, 2]:
        bst.insert(key, value=None)
    print('preOrder')
    bst.preOrder()
    print('inOrder')
    bst.inOrder()
    print('postOrder')
    bst.postOrder()
    print('SequenceOrder')
    bst.SequenceOrder()
    bst.remove(6)
    print('inOrder')
    bst.inOrder()
    bst.removemax()
    print('inOrder')
    bst.inOrder()








