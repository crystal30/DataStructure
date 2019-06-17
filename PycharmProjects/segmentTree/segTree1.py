# -*- coding: utf-8 -*-
#区间树／线段树
class SegTree:
    def __init__(self,data):
        self.__data = data
        self.__n = len(self.__data)
        self.__tree = [None]*self.__n*4
        self.__subTree(0,0,self.__n-1)

    def __subTree(self,ti,l,r):
        if l == r:
            self.__tree[ti] = self.__data[l]
            # self.__tree[ti] = [self.__data[l]]
            return

        mid = l + (r-l)//2
        self.__subTree(ti * 2 + 1, l, mid)
        self.__subTree(ti * 2 + 2, mid + 1, r)
        self.__tree[ti] = self.__merger(self.__tree[ti*2+1], self.__tree[ti*2 +2])
    def query(self,ql,qr):
        return self.__query(ql,qr,0,self.__n-1,0)

    def __query(self,ql,qr,l,r,ti):
        if ql<= l and qr>= r:
            return self.__tree[ti]
        if ql > r or qr < l:
            return 0
        else:
            mid = l + (r-l)//2
            return self.__merger(self.__query(ql,qr,l,mid,ti*2+1),self.__query(ql,qr,mid+1,r,ti*2+2))

    #融合器，求和
    def __merger(self,a,b):
        return a+b

    def set(self,i,e):
        self.__set(i,e,0,0,self.__n-1)

    def __set(self,i,e,ti,l,r):
        if l == r:
            self.__tree[ti] = e
            return

        mid = l + (r-l)//2
        if i >= mid+1:
            self.__set(i,e,ti*2+2,mid+1,r)
        if i <= mid:
            self.__set(i,e,ti*2+1,l,mid)
        self.__tree[ti] = self.__merger(self.__tree[ti*2+1], self.__tree[ti*2+2])


    def __str__(self):
        return str(self.__tree)

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    seg = SegTree(nums)
    print(seg)
    print(seg.query(2,3))
    seg.set(2,5)
    print(seg)
