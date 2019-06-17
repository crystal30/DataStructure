class TestProgram:

    #针对有顺序数组的二分查找法,若存在目标元素，返回目标元素的下标，若不存在，返回-1
    #时间复杂度 O(logn)
    @classmethod
    def binarySearch(cls, arr, target):
        r = len(arr)-1
        l = 0
        while l <= r:
            m = l + (r - l) // 2
            if target == arr[m]:
                return m
            elif target > arr[m]:
                l = m+1
            else:
                r = m-1
        return -1


    #在一个数组中找到最大的元素，并返回该最大元素
    #时间复杂度O(n)
    @classmethod
    def findMax(cls, arr):
        maxIndex = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[maxIndex]:
                maxIndex = i

        return arr[maxIndex]


    #归并排序，自底向上，不需要用到递归
    #从小到大排序,时间复杂度O(nlogn)
    @classmethod
    def mergSort(cls, arr):
        n = len(arr)
        sz = 1
        while sz < n:
            temp = arr.copy()
            for i in range(0, n, 2*sz):
                cls.__merge(arr, i, i+sz-1, min(i+2*sz-1, n-1), temp)
            sz += sz
        return arr

    @classmethod
    def __merge(cls, arr, l, mid, r, temp):
        '''

        :param arr: 原始的数组
        :param l: 表示要归并的两部分合起来的起始位置
        :param mid:表示要归并的两部分的中间位置，即第二部分初始下标的前一个位置。
        :param r: 表示要归并的两部分合起来的终止位置[l,...r]是前闭后闭的闭区间
        :param temp: 归并排序时需要的额外空间
        :return:
        '''
        i = l
        j = mid+1
        for k in range(l, r+1):
            if i>mid:
                arr[k] = temp[j]
                j += 1
            elif j>r:
                arr[k] = temp[i]
                i += 1
            elif temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1


    #选择排序，时间复杂度为O(n2)
    @classmethod
    def selectionSort(cls, arr):
        n = len(arr)
        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr








