#运行速度较SelectionSort1 快
import random
from maxHeap import MaxHeap
from copy import copy

class Sort():

    #时间复杂度为O（n2）的排序算法
    # 从小到达排序
    @classmethod
    def selectionSort(cls, arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[minIndex], arr[i] = arr[i], arr[minIndex]

        return arr

    @classmethod
    def insertionSort(cls, arr):
        for i in range(1, len(arr)-1):
            for j in range(i+1,0,-1):
                if arr[j] < arr[j-1]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
                else:
                    break
        return arr

    @classmethod
    def improveInsertionSort(cls, arr):
        for i in range(1, len(arr) - 1):
            finalIndex = i # 最终要插入的位置
            e = arr[i+1] #保存要插入的元素的值
            for j in range(i + 1, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j] = arr[j-1]
                    finalIndex = j-1
                else:
                    break
            arr[finalIndex] = e
        return arr



    @classmethod
    def bubbleSort(cls, arr):
        n = len(arr)
        while n>=2:
            for i in range(n-1):
                if arr[i+1] < arr[i]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                n = n-1
        return arr

    @classmethod
    def improveBubbleSort(cls, arr):
        n = len(arr)
        while n >= 2:
            j = 0  #在从小到大排序中，存放最大的元素的下标
            for i in range(1,n):
                if arr[j] < arr[i]:
                    j = i       #此时不需要互换两个元素，只需要更改下标即可
            arr[j], arr[n-1] = arr[n-1], arr[j] # 最终，排序区域中最大的下标与最后一个元素互换
            n = n-1
        return arr

    @classmethod
    # 1, 4, 13, 40, 121, 364, 1093...
    #从小到大排序
    def shellSort(cls, arr):
        n = len(arr)
        increment = n//3 + 1
        while increment>=1:
            for i in range(increment, n):
                e = arr[i]
                j = i    #j存放排序范围的最小的元素下标
                while j >= increment and e < arr[j-increment]:
                    arr[j] = arr[j-increment]
                    j -= increment
                arr[j] = e
            increment = increment//3
        return arr

    #时间复杂度为ONlog(N)

    @classmethod
    #自顶向下的归并排序
    def MergeSort(cls, arr):
        cls.__mergeSort(arr, 0, len(arr) - 1)
        return arr

    # 在[l,r]这个区间内进行归并排序
    @classmethod
    def __mergeSort(cls, arr, l, r):
        mid = l + (r - l) // 2

        #改进递归终止的条件，数据量越小，越可能是有序的，而插入排序对近乎有序的数据具有天然的优势；
        #另一方面，在数据量比较小时，O（n2）与O（nlogn）的差别不是很明显，且说插入排序复杂度前面
        # 的常数更小，不是很理解，插入排序的复杂度也有可能降到O（n）.
        #综上，在数据量较小时，结束递归，用插入排序
        if r-l <= 15:
            return cls.__insertionSort(arr, l, r)
        # if l >= r:
        #     return

        if l < r:
            cls.__mergeSort(arr, l, mid)
            cls.__mergeSort(arr, mid + 1, r)
            #做一个小小的改进,此时 arr[l,mid], arr[mid+1,r]都是有序的，
            # 如果，arr[mid]<arr[mid+1] 时，arr[l,r]将都是有序的，故不再需要归并那一步
            if arr[mid+1] < arr[mid]:
                cls.__merge(arr, l, r, mid)
    #将排好序的子区间两两归并
    @classmethod
    def __merge(cls, arr, l, r, mid):
        i = l
        j = mid + 1
        temp = [None] * (r - l + 1)
        for k in range(r - l + 1):
            if j > r:
                temp[k] = arr[i]
                i += 1
            elif i > mid:
                temp[k] = arr[j]
                j += 1
            elif arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            elif arr[j] < arr[i]:
                temp[k] = arr[j]
                j += 1
        arr[l:r + 1] = temp

    @classmethod
    def __insertionSort(cls, arr, l, r):
        for i in range(l, r):
            for j in range(i+1, l, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                else:
                    break

    @classmethod
    #自底向上的归并排序
    #此种方法可以很好的用于对链表的排序
    def MergeSortBU(cls, arr):
        n = len(arr)
        size = 1 # 表示归并的两个子序列的长度，初始长度为1
        while size<n:
            for i in range(0,n,size*2):
                l = i
                r = min(n-1,i+2*size-1)
                cls.__merge(arr,l, r, l+size-1)
            size = size*2
        return arr

    @classmethod
    # 自底向上的归并排序
    def improveMergeSortBU(cls, arr):
        # 同自顶向下的归并排序一样，可以对两个地方进行改进
        # 1. 当数组的数据量比较小时，可以分别对两个需要归并的子序列使用插入排序
        # 2. 在归并时加入条件判断，当arr[mid] < arr[mid+1] 时不需要进行归并，
        # 因为这两个子序列本来就是有序的。
        n = len(arr)
        i = 0
        #改进1
        while i<n:
            cls.__insertionSort(arr, i, min(n-1,i+15))
            i += 16
        size = 16  # 表示归并的两个子序列的长度，初始长度为16
        while size < n:
            for i in range(0, n-size, size * 2):
                l = i
                r = min(n-1,i + 2 * size - 1)
                # mid = l + (r - l) // 2
                #改进2
                if arr[l+size] < arr[l+size-1]:
                    cls.__merge(arr, l, r, l+size-1)
            size = size * 2
        return arr

    @classmethod

    def quickSort(cls, arr):
        cls.__quickSort(arr, 0, len(arr)-1)
        return arr

    @classmethod
    def __quickSort(cls, arr, l, r):
        #改进1
        if r - l <=15:
            cls.__insertionSort(arr, l, r)
            return
        # if r <= l:
        #     return
        j = cls.__partition(arr, l, r)
        cls.__quickSort(arr, l, j-1)
        cls.__quickSort(arr, j+1, r)

    @classmethod
    #返回p，使得 arr[l,1,2,...j-1]< arr[j] < arr[j+1,.....r]
    def __partition(cls, arr, l, r):

        #改进1
        #返回一个随机整数N，a <= N <= b
        t = random.randint(l,r)
        arr[l], arr[t] = arr[t], arr[l]
        j = l
        #arr[l+1,.....j] <arr[l] < arr[j+1,....i)
        for i in range(l + 1, r + 1):
            if arr[i] < arr[l]:
                arr[i], arr[j + 1] = arr[j + 1], arr[i]
                j += 1
        arr[l], arr[j] = arr[j], arr[l]
        return j

    @classmethod
    def quickSort2(cls, arr):
        cls.__quickSort2(arr, 0, len(arr)-1)
        return arr

    @classmethod
    def __quickSort2(cls, arr, l, r):
        #改进1
        if r - l <=15:
            cls.__insertionSort(arr, l, r)
            return
        # if r <= l:
        #     return
        j = cls.__partition2(arr, l, r)
        cls.__quickSort2(arr, l, j-1)
        cls.__quickSort2(arr, j+1, r)


    @classmethod
    def __partition2(cla, arr, l, r):
        # 改进1
        # 返回一个随机整数N，a <= N <= b
        t = random.randint(l, r)
        arr[l], arr[t] = arr[t], arr[l]
        i = l + 1
        j = r
        # arr[l+1,.....j] <arr[l] < arr[j+1,....i)
        while True:
            while i <= r and arr[i] < arr[l]:
                i += 1
            while j >= l+1 and arr[j] > arr[l]:
                j -= 1
            if i>j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        arr[l], arr[j] = arr[j], arr[l]
        return j

    @classmethod
    def quickSort3(cls, arr):
        cls.__quickSort3(arr, 0, len(arr) - 1)
        return arr

    @classmethod
    def __quickSort3(cls, arr, l, r):
        # 改进1
        if r - l <= 15:
            cls.__insertionSort(arr, l, r)
            return
        # if r <= l:
        #     return
        lt, gt = cls.__partition3(arr, l, r)
        cls.__quickSort3(arr, l, lt)
        cls.__quickSort3(arr, gt, r)

    @classmethod
    def __partition3(cls, arr, l, r):
        # 改进1
        # 返回一个随机整数N，a <= N <= b
        t = random.randint(l, r)
        arr[l], arr[t] = arr[t], arr[l]

        lt = l
        i = l + 1
        gt = r + 1
        v = arr[l]
        # [l,lt]中存放< v的数；[gt,r]中存放>v的数；[lt+1,gt-1]存放=v的数
        while i<gt:
            if arr[i] < v:
                arr[lt + 1], arr[i] = arr[i], arr[lt + 1]
                i += 1
                lt += 1
            elif arr[i] > v:
                arr[gt - 1], arr[i] = arr[i], arr[gt - 1]
                gt -= 1
            else: # arr[i] < v
                i += 1
        arr[l], arr[lt] = arr[lt], arr[l]
        lt -= 1
        return lt, gt

    @classmethod
    def heapSort1(cls,arr):
        maxheap = MaxHeap()
        for i in arr:
            maxheap.add(i)
        for i in range(len(arr)-1,-1,-1):
            arr[i] = maxheap.extraMax()
        return arr

    @classmethod
    #改进1：用heapify 直接将数组放入堆中，从最后一个不是叶子节点的节点进行下沉操作，
    # 使其满足最大堆的性质；然后再用推出堆顶的最大（优先级最高）的元素，放入新的数组空间中
    #此时，需要额外的开辟len（arr）的空间，能不能不开新的空间呢，见heapSort3
    def heapSort2(cls, arr):
        #注意：需要重新拷贝一下，因为heapify和extraMax是直接
        # 在maxheap.heapify(arr1)中传入的arr1上操作的，最终arr1已经是空的了
        #这样，如果不拷贝的话，传进来的arr就变成了空数组，在测试用例中就不能再进行下边的操作了，
        # 除非生成一个新的实例（因为测试用例的数组实在构造函数中生成的）
        arr1 = copy(arr)
        maxheap = MaxHeap()
        maxheap.heapify(arr1)
        temp = [None] * len(arr1)
        for i in range(len(arr1)-1,-1,-1):
            temp[i] = maxheap.extraMax()
        return temp


    @classmethod
    # 改进：原地堆排序
    #注意，此处为原地堆排序，也存在heapSort2中的问题，我们是直接在arr上操作的，
    # 如果不拷贝的话，传进来的arr就变成了从小到大排序的数组，在测试用例中的self.nums也变成了从小到大排序的，
    # 除非生成一个新的实例（因为测试用例的数组实在构造函数中生成的）
    def heapSort3(cls, arr):
        n = len(arr) - 1
        p = (n - 1) // 2  # 第一个不是叶子节点的节点（下标从0开始算）
        for i in range(p, -1, -1):
            cls.__shiftDown(arr, n, i)
        for i in range(n):
            arr[0], arr[n - i] = arr[n - i], arr[0]
            cls.__shiftDown(arr, n - 1 - i, 0)
        return arr

    # 在下标范围内进行下沉操作
    @classmethod
    def __shiftDown(cls, arr, r, p):
        '''

        :param arr:
        :param r:   要生成最大堆的数组arr[:r]
        :param p: 要下沉的元素坐标
        :return:
        '''
        # l = i*2+1
        # r = i*2+2
        # p = (i-1)//2
        l = p * 2 + 1  # 节点p的左孩子
        while l <= r:
            j = l  # j中存放的是要与arr[p]交换的元素
            if j + 1 <= r and arr[j] < arr[j + 1]:
                j += 1
            if arr[p] < arr[j]:
                arr[p], arr[j] = arr[j], arr[p]
                p = j
                l = p * 2 + 1
            else:
                break

































