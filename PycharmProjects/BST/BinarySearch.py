#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#在有序的数组中，查找目标元素target，若target在数组中，返回target的下标，若不在该数组中，返回-1
class BinarySearch():

    #1. 用递归的方式实现  二分查找法
    @classmethod
    def bS1(cls,arr,target):
        n = len(arr)
        #递归结束的条件
        return cls.__bs(arr, 0, n-1, target)


    #搜索范围 arr[l,r],前闭后闭。
    @classmethod
    def __bs(cls, arr, l, r, target):

        #当还剩一个元素时，此时不能再进行分割，所以，看一下此时这个元素是否等于target
        #等于，就就返回target的小标，不等于返回-1
        if l == r:
            return l if target == arr[l] else -1

        mid = l + (r-l)//2
        #由于每个分支路下边都有return，所以，可以用if，if，if 也可以用if，elif, else,效果是一样的
        if target < arr[mid]:
            return cls.__bs(arr, l, mid-1, target)
        elif target > arr[mid]:
            return cls.__bs(arr, mid+1, r, target)
        else: #target == arr[mid]:
            return mid

    # 2.用非递归的方式实现 二分查找法
    # 查找的范围是arr[l,r], 前闭后闭的范围
    @classmethod
    def bS2(cls, arr, target):
        n = len(arr)
        l = 0
        r = n-1
        while l<=r:
            mid = l + (r - l) // 2
            if target < arr[mid]:
                r = mid-1
            elif target > arr[mid]:
                l = mid+1
            else:
                return mid
        return -1

    #对于binarySearch1 binarySearch2，其对具有重复元素的有序数组，就不知道他到底输出的是第几个重复元素的下标
    #eg：当arr = [3,3,4,5,6,7] ,target=3 时，输出 为0；当arr = [3,3,3,4,5,6,7]，target=3时，输出为 1
    #为什么 binarySearch1 binarySearch2中，对于重复的元素，其输出的下标不确定呢？
    ##因为，首先将检索查找范围中的中间元素，所以重复元素所处的位置不同，处在可能被作为mid的位置的重复元素，越先被检索到，输出其下标
    #如果我们 要想输出重复元素的第一个小标或是最后一个下标该如何做呢？
    #见floor, ceil

    # 二分查找法, 在有序数组arr中, 查找target
    # 如果找到target, 返回第一个target相应的索引index
    # 如果没有找到target, 返回比target小的最大值相应的索引, 如果这个最大值有多个, 返回最大索引
    # 如果这个target比整个数组的最小元素值还要小, 则不存在这个target的floor值, 返回 - 1
    @classmethod
    def floor(cls, arr,target):
        n = len(arr)
        l = 0
        r = n-1
        while l<r:
            mid = l + (r - l) // 2
            if target <= arr[mid]:
                r = mid
            else:#target > arr[mid]
                l = mid + 1
        assert l==r, "That time l should be equal r"

        if target == arr[l]:
            return l
        else:
            return l-1

    # 二分查找法, 在有序数组arr中, 查找target
    # 如果找到target, 返回最后一个target相应的索引index
    # 如果没有找到target, 返回比target大的最小值相应的索引, 如果这个最小值有多个, 返回最小索引
    # 如果这个target比整个数组的最大元素值还要大, 则不存在这个target的floor值, 返回 - 1
    @classmethod
    def ceil(cls, arr,target):
        n = len(arr)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            if target < arr[mid]:
                r = mid
            else: #target >= arr[mid]
                l = mid+1
        assert l == r, "This time l should be equal r"
        if target == arr[r]:
            return r
        else:
            return r+1 if r+1<n else -1


if __name__ == '__main__':
    # arr = [3,3,3,3,4,5,6,7]
    arr = [40,40,40,40, 41, 41, 41, 41,43, 43, 44]
    target = 45
    # print(binarySearch1(arr, target))
    # print(binarySearch2(arr, target))
    BS = BinarySearch()
    re1 = BS.floor(arr, target)
    re2 = BS.ceil(arr, target)
    print(re1)
    print(re2)





