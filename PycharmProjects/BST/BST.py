#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class BST:
    class __Node():
        def __init__(self,e=None):
            self.e = e
            self.left = None
            self.right = None
        def __repr__(self):
            return str(self.e)

    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0
    #
    # # 添加元素1
    # def add(self,e):
    #
    #     if self.root == None:
    #         self.root = self.__Node(e)
    #         self.size += 1
    #     else:
    #         self.__addNode(self.root, e)
    #
    # # 向以Node为根的二分搜索树中插入元素e,递归算法
    # def __addNode(self,Node,e):
    #     if Node.e == e:
    #         return
    #     elif Node.e > e and Node.left == None:
    #         Node.left = self.__Node(e)
    #         self.size += 1
    #         return
    #     elif Node.e < e and Node.right == None:
    #         Node.right = self.__Node(e)
    #         self.size += 1
    #         return
    #
    #     if Node.e > e:
    #         self.__addNode(Node.left, e)
    #     else:
    #         self.__addNode(Node.right, e)

    # 添加元素2
    def add(self,e):
        self.root = self.__add(self.root, e)

    # 返回新插入节点后，二分搜索树的根
    def __add(self,Node,e):
        if Node is None:
            self.size += 1
            return self.__Node(e)

        if Node.e > e:
            Node.left = self.__add(Node.left, e)
        elif Node.e < e:
            Node.right = self.__add(Node.right, e)

        return Node

    # 看二分搜索树是否含有元素e
    def contains(self, e):
        return self.__contains(self.root, e)

    def __contains(self, Node, e):

        if Node == None:
            return False
        else:
            if Node.e == e:
                return True
            elif Node.e > e:
                return self.__contains(Node.left, e)
            else:
                return self.__contains(Node.right, e)

    #二分搜索树的前序遍历
    def preOrder(self):
        return self.__preOrder(self.root)

    def __preOrder(self, Node):

        if Node == None:
            return
        print(Node.e)
        self.__preOrder(Node.left)
        self.__preOrder(Node.right)

    #二分搜索树的中序遍历
    def inOrder(self):
        return self.__inOrder(self.root)

    def __inOrder(self, Node):
        if Node == None:
            return
        self.__inOrder(Node.left)
        print(Node.e)
        self.__inOrder(Node.right)

    #二分搜索树的后序遍历
    def postOrder(self):
        return self.__postOrder(self.root)

    def __postOrder(self, Node):
        if Node == None:
            return
        self.__postOrder(Node.left)
        self.__postOrder(Node.right)
        print(Node.e)

    #层序遍历
    def levelOrder(self):
        queue = []
        if self.root == None:
            return
        queue.append(self.root)

        while len(queue) != 0:
            cur = queue.pop(0)
            print(cur.e)
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

    #搜索BST中的最小值
    def minimum(self):
        return self.__minimum(self.root).e

    # 返回以node为根的二分搜索树的最小值所在的节点
    def __minimum(self,Node):

        if Node.left == None:
            return Node

        return self.__minimum(Node.left)

    #删除BST中的最小值,并返回最小值
    def removeMin(self):
        re = self.minimum()
        self.root = self.__removeMin(self.root)
        return re

    #删除掉以node为根的二分搜索树中的最小节点
    #返回删除节点后新的二分搜索树的根
    def __removeMin(self,Node):

        if Node.left == None:
            rightNode = Node.right
            self.size -= 1
            return rightNode
        Node.left = self.__removeMin(Node.left)
        return Node


    # 搜索BST中的最大值
    def maximum(self):
        return self.__maximum(self.root).e

    # 返回以node为根的二分搜索树的最大值所在的节点
    def __maximum(self, Node):

        if Node.right == None:
            return Node

        return self.__maximum(Node.right)

    # 删除BST中的最大值,并返回最大值
    def removeMax(self):
        re = self.maximum()
        self.root = self.__removeMax(self.root)
        return re

    # 删除掉以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def __removeMax(self, Node):

        if Node.right == None:
            leftNode = Node.left
            self.size -= 1
            return leftNode

        Node.right = self.__removeMax(Node.right)
        return Node

    #删除任意元素
    def remove(self,e):
        self.root = self.__remove(self.root, e)
    # 删除掉以node为根的二分搜索树中值为e的节点, 递归算法
    # 返回删除节点后新的二分搜索树的根
    def __remove(self, Node, e):
        if Node == None:
            return
        if Node.e > e:
            Node.left = self.__remove(Node.left, e)
        elif Node.e < e:
            Node.right = self.__remove(Node.right, e)
        else:
            # 要删除的节点左子树为空的情况
            if Node.left == None:
                rightNode = Node.right
                Node.right = None
                self.size -= 1
                return rightNode

            # 要删除的节点右子树为空的情况
            if Node.right == None:
                leftNode = Node.left
                Node.left = None
                self.size -= 1
                return leftNode

            # 要删除的节点 左子树和右子数均不为空
            # 找到该节点右子树中最小的节点，成为该节点的后继 sNode
            # 删除该节点右子树最小的节点（sNode），并让sNode.right指向此右子树，
            # sNOde.left 指向该节点的左子树 至此，sNode 已经占据了要删除的节点的位置
            # 删除Node，令Node.right 和 Node.left 均为 None，size --
            if Node.left != None and Node.right != None:

                sNode = self.__minimum(Node.right)
                sNode.right = self.__removeMin(Node.right)
                sNode.left = Node.left
                Node.right = Node.left = None
                return sNode
        return Node

if __name__ == '__main__':
    bst = BST()
    for key in [5, 3, 6, 8,4, 2]:
        bst.add(key)
    print('preOrder')
    bst.preOrder()
    print('inOrder')
    bst.inOrder()
    print('postOrder')
    bst.postOrder()
    bst.remove(6)
    print('inOrder')
    bst.inOrder()














