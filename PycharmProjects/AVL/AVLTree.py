#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class AVLTree:
    class __Node():
        def __init__(self,key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.hight = 1
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
            #看一下此处是否应该直接return
            return self.__Node(key,value)


        if Node.key > key:
            Node.left = self.__add(Node.left, key, value)
        elif Node.key < key:
            Node.right = self.__add(Node.right, key, value)

        #更新节点的hight
        Node.hight = 1 + max(self.getHight(Node.left), self.getHight(Node.right))
        balanceFactor = self.getBalanceFactor(Node)
        # if abs(balanceFactor) > 1:
        #     print('unblance: balanceFactor is ', balanceFactor)

        # LL
        if balanceFactor > 1 and self.getBalanceFactor(Node.left) >= 0:
            #左子树太深了，打破了平衡，右旋
            return self.__rightRotate(Node)
        #RR
        if balanceFactor < -1 and self.getBalanceFactor(Node.right) <= 0:
            #右子树太深了，打破了平衡，左旋
            return self.__leftRotate(Node)
        #LR
        if balanceFactor > 1 and self.getBalanceFactor(Node.left) <= 0:
            Node.left = self.__leftRotate(Node.left)
            return self.__rightRotate(Node)

        # RL
        if balanceFactor < -1 and self.getBalanceFactor(Node.right) >= 0:
            Node.right = self.__rightRotate(Node.right)
            return self.__leftRotate(Node)

        return Node

    # 对节点y进行向右旋转操作，返回旋转后新的根节点x
    #       y
    #      / \                                  x
    #     x  T4          向右旋转               /   \
    #    / \          - - - - - - - ->       z     y
    #   z  T3                               / \  /  \
    #  / \                                 T1 T2 T3 T4
    # T1 T2
    def __rightRotate(self, y):

        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        #更新一下树的高度，T1，T2, T3, T4, Z的高度不变，只用更新 x和y的即可
        y.hight = 1 + max(self.getHight(y.left), self.getHight(y.right))
        x.hight = 1 + max(self.getHight(x.left), self.getHight(x.right))
        return x

    # 对节点y进行向右旋转操作，返回旋转后新的根节点x
    #       y
    #      / \                                   x
    #     T4  x          向左旋转               /   \
    #        / \      - - - - - - - ->       y     z
    #       T3 z                            / \   /  \
    #         / \                          T4 T3 T1 T2
    #        T1 T2

    def __leftRotate(self, y):

        x = y.right
        T3 = x.left

        x.left = y
        y.right = T3

        #更新一下树的高度，T1，T2, T3, T4, Z的高度不变，只用更新 x和y的即可
        y.hight = 1 + max(self.getHight(y.left), self.getHight(y.right))
        x.hight = 1 + max(self.getHight(x.left), self.getHight(x.right))
        return x
    def getHight(self,Node):
        if Node is None:
            return 0
        else:
            return Node.hight

    def getBalanceFactor(self,Node):
        return self.getHight(Node.left)- self.getHight(Node.right)

    def isBalance(self):
        return self.__isBalance(self.root)

    def __isBalance(self, Node):
        if Node == None:
            return True

        if self.getBalanceFactor(Node) <= 1:
            return self.__isBalance(Node.right) and self.__isBalance(Node.left)
        else:
            return False

    def isBST(self):
        keys = []
        self.inOrder(self.root,keys)
        for i in range(len(keys)-1):
            if keys[i] > keys[i+1]:
                return False
        return True
    #中序遍历
    def inOrder(self,Node,keys):

        if Node == None:
            return

        self.inOrder(Node.left, keys)
        keys.append(Node.key)
        self.inOrder(Node.right, keys)
        return keys

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
            retNode = Node

        elif Node.key < key:
            Node.right = self.__remove(Node.right, key)
            retNode =  Node
        else:
            if Node.right == None:
                leftNode = Node.left
                Node.left = None
                self.size -= 1
                retNode = leftNode

            elif Node.left == None:
                rightNode = Node.right
                Node.right = None
                self.size -= 1
                retNode = rightNode

            elif Node.left != None and Node.right != None:
                minNode = self.__minimum(Node.right)
                # minNode.right = self.__removeMin(Node)
                minNode.right = self.__remove(Node.right,minNode.key)
                minNode.left = Node.left
                Node.left, Node.right = None, None
                retNode = minNode

            if retNode == None:
                return None
            else:
                # 更新节点的hight
                retNode.hight = 1 + max(self.getHight(retNode.left), self.getHight(retNode.right))
                balanceFactor = self.getBalanceFactor(retNode)

                # LL
                if balanceFactor > 1 and balanceFactor(retNode.left) >= 0:
                    # 左子树太深了，打破了平衡，右旋
                    return self.__rightRotate(retNode)
                # RR
                if balanceFactor < -1 and balanceFactor(retNode.right) <= 0:
                    # 右子树太深了，打破了平衡，左旋
                    return self.__leftRotate(retNode)
                # LR
                if balanceFactor > 1 and balanceFactor(retNode.left) <= 0:
                    Node.left = self.__leftRotate(retNode.left)
                    return self.__rightRotate(retNode)

                # RL
                if balanceFactor < -1 and balanceFactor(retNode.right) >= 0:
                    Node.right = self.__rightRotate(retNode.right)
                    return self.__leftRotate(retNode)

                return retNode



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
    link = AVLTree()
    words = ['12','12','34','56','56','12','38','39','40','41']
    for word in words:
        if link.contains(word):
            link.set(word, link.get(word)+1)
        else:
            link.add(word,1)
    print(link.isBalance())
    print(link.isBST())
    setwords = set(words)
    for word in setwords:
        link.remove(word)
        if not link.isBalance():
            print('not balanced ')
        if not link.isBST():
            print('not BST ')










