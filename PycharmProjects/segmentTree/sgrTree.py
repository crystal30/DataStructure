#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SegTree():
    def __init__(self, data):
        self.__data = data
        self.__tree = [None]*len(data)*4


    def getSize(self):
        return len(self.__data)

    def getIndex(self, index):
        return self.getIndex(index)

    # 左孩子节点
    def __leftChild(self, index):
        return index*2 + 1

    # 右孩子节点
    def __rightChild(self, index):
        return index*2 + 2

    #融合函数，这里 返回 两个list 相加
    def merger(self, a,b):
        return a+b

    def tree(self):
        self.__subTree(0,l=0, r = len(self.__data)-1)

    def __subTree(self,index,l, r):
        if l==r:
            # self.__tree[index] = [self.__data[l]]
            self.__tree[index] = self.__data[l]
            return
        else: # l<r

            mid = (r+l) // 2
            lChild = self.__leftChild(index)
            rChild = self.__rightChild(index)

            self.__subTree(lChild, l,mid)
            self.__subTree(rChild, mid+1,r)
            self.__tree[index] = self.merger(self.__tree[lChild], self.__tree[rChild])

    #查询
    def query(self,ql, qr):
        return self.__query(0, 0, len(self.__data)-1, ql, qr)

    def __query(self,treeIndex, l, r, ql, qr):
        if l==ql and r == qr:
            return self.__tree[treeIndex]
        leftChild = self.__leftChild(treeIndex)
        rightChild = self.__rightChild(treeIndex)
        mid = (l+r) // 2

        if qr <= mid:
            return self.__query(leftChild, l, mid, ql, qr)
        elif ql >= mid+1:
            return self.__query(rightChild, mid+1, r, ql, qr)

        if ql <= mid and qr > mid:
            leftRe = self.__query(leftChild,l,mid,ql, mid)
            rightRe = self.__query(rightChild, mid+1, r, mid+1, qr)
            return self.merger(leftRe , rightRe)

    #更新
    def set(self,index,e):
        self.__data[index] = e
        self.__set(0, 0, len(self.__data)-1, index,e)

    def __set(self,treeIndex, l, r, index ,e):
        if l == r:
            # self.__tree[treeIndex] = [e]
            self.__tree[treeIndex] = e
            # self.__tree[treeIndex] = [self.__data[l]]
            return
        mid = l + (r-l)//2
        leftChild = self.__leftChild(treeIndex)
        rightChild = self.__rightChild(treeIndex)
        if index <= mid:
            self.__set(leftChild,l,mid,index,e)
        elif index >= mid+1:
            self.__set(rightChild, mid+1, r, index, e)

        self.__tree[treeIndex] = self.merger(self.__tree[leftChild], self.__tree[rightChild])

    def __str__(self):
        return str(self.__tree)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    seg = SegTree(nums)
    seg.tree()
    print(seg)
    print(seg.query(2,3))
    seg.set(2,5)
    print(seg)


