# -*- coding: utf-8 -*-

__author__ = 'xl'
"""
__date__ = TIME： 2018/10/03 下午4:13
describe:
"""
from random import randint

# 从alist的某个节点k开始下沉，n = len(alist)
def fixDown(alist,k,n):
    while k*2 < n:    #K*2 为k的左孩子
        if 2*k+1 >n:  #k*2+1 为k的右孩子
            max_children = 2*k
        else:
            if alist[2*k]>alist[2*k+1]:
                max_children = 2*k      #这个条件下和上个条件下 做执行的均是max_children = 2*k，可以合并？
            else:
                max_children = 2*k+1
        #改进，可以将上边的进行简化

        if alist[k]<alist[max_children]:
            alist[k],alist[max_children]=alist[max_children],alist[k]
            k = max_children
        else:
            break


def heap_sort(alist):
    alist =[0]+ alist[:]
    n = len(alist)-1
    for i in range(n//2,0,-1):
        fixDown(alist,i,n)
    #至此，已经将heap_sort 改造成了最小堆，时间复杂度为O(n)

    #再用最小堆对数组排序，时间复杂度O(nlogn)
    for i in range(n):
        alist[n],alist[1]=alist[1],alist[n]
        n -= 1
        fixDown(alist,1,n)
    return alist[1:]

#改进：可以不加alist =[0]+ alist[:] 这条指令，
#当list的index是从0开始时，将list以heapify的方式转化为最小堆，节点i的父节点是：(i-1)//2,节点i的左孩子是i*2+1,右孩子是 i*2+2
#当list的index是从1开始(等价于你的 alist =[0]+ alist[:])，节点i的父节点是：i//2,节点i的左孩子是i*2,右孩子是 i*2+1


#按照你的思路，list的index是从1开始的
#heap_sort没变
def heap_sort1(alist):
    alist =[0]+ alist[:]
    n = len(alist)-1
    for i in range(n//2,0,-1):
        shiftDown1(alist,i,n)
    #至此，已经将heap_sort 改造成了最小堆，时间复杂度为O(n)

    #再用最小堆对数组排序，时间复杂度O(nlogn)
    for i in range(n):
        alist[n],alist[1]=alist[1],alist[n]
        n -= 1
        fixDown(alist,1,n)
    return alist[1:]

#shiftDown的操作有所改进
def shiftDown1(alist, k, n):
    j = 2*k  # j 最终为k 左右孩子中数值较小的孩子
    while (j < n):
        if j + 1 < n and alist[j] > alist[j+1]:
            j += 1

        if alist[j] < alist[k]:
            alist[j], alist[k] = alist[k],alist[j]
            # k = j
            # j = 2*k
            j = 2*j
        else:
            break

#list坐标是从0开始的，感觉这种更加简洁
def heap_sort2(alist):
    n = len(alist)-1
    for i in range((n-1)//2,-1,-1):
        shiftDown2(alist,i,n)
    #至此，已经将heap_sort 改造成了最小堆，时间复杂度为O(n)

    #再用最小堆对数组排序，时间复杂度O(nlogn)
    for i in range(n):
        alist[n],alist[0]=alist[0],alist[n]
        n -= 1
        fixDown(alist,0,n)
    return alist

#shiftDown的操作有所改进
def shiftDown2(alist, k, n):
    j = 2*k+1  # j 最终为k 左右孩子中数值较小的孩子
    while (j < n):
        if j + 1 < n and alist[j] > alist[j+1]:
            j += 1
        if alist[j] < alist[k]:
            alist[j], alist[k] = alist[k],alist[j]
            # k = j
            # j = 2*k +1
            j = 2*j +1
        else:
            break

if __name__ == "__main__":
    print('hellp')
    ll = [randint(1,20000) for x in range(100)]
    print(heap_sort(ll))