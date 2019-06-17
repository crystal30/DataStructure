# !usr/bin/env python3
#-*- coding: utf-8 -*-
import time
#二分查找法 针对有序数组
class BinarySearch:

    # 下边几种均是非递归的二分搜索算法，只不过定义的边界不同
    # 搜索范围[l, r]前闭后开
    @classmethod
    def bs1(cls, arr, target):
        '''

        :param arr:排好序的数组
        :param target: 所要搜寻的目标元素
        :return: 若target在数组中，返回target所在的下标；若 target不在数组中，返回-1
        '''
        l = 0 #搜寻范围的左边界
        r = len(arr) - 1 #搜寻范围的右边界，即搜寻范围为[l,r],前闭后闭

        while l <= r:
        #到底是l<r,还是 l<=r呢，
        # 思考：当l<r时，最终搜寻范围[l,r]中有两个元素，当l<=r时，最终搜寻范围[l,r]中还剩1个元素
            mid = l + (r-l)//2
            if target == arr[mid]:
                return mid

            if target > arr[mid]:
                l = mid+1 #为什么l=mid+1,而不是 l=mid呢。
                          # 再次看初始的定义，搜寻范围为[l,r],前闭后闭，已经知道arr[mid] != target,
                          # 所以搜索范围就没有必要再包括arr[mid]了

            else:#target < arr[mid]
                r = mid-1 #为什么r=mid-1,而不是 r=mid呢? 同上

        return -1

    #搜索范围[l, r)前闭后开
    @classmethod
    def bs2(cls, arr, target):
        l = 0
        r = len(arr)
        #搜索范围[l,r)前闭后开
        while l<r:  #当 l== r时，[l,r)区间是无效的.
            mid = l + (r-l)//2
            if target == arr[mid]:
                return mid

            if target > arr[mid]:
                l = mid + 1
            else:#target < arr[mid]
                r = mid
        return -1


    # 搜索范围(l, r)前开后开
    @classmethod
    def bs3(cls, arr, target):
        l = -1
        r = len(arr)
        while l < r-1:
            mid = l + (r-l)//2
            if target == arr[mid]:
                return mid
            if target > arr[mid]:
                l = mid
            else:#target < arr[mid]
                r = mid
        return -1


if __name__ == "__main__":
    arr = [_ for _ in range(10000)]
    start = time.time()
    for i in arr:
        assert i == BinarySearch.bs1(arr, i), " There is a error in bs1"
        assert i == BinarySearch.bs2(arr, i), " There is a error in bs2"
        assert i == BinarySearch.bs3(arr, i), " There is a error in bs3"
    end = time.time()
    print(end - start)


