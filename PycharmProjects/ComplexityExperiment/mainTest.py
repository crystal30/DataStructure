from TestData import TestData
from TestProgram import TestProgram
import time

#测试binarySearch,时间复杂度为O(logn),可以看到随着数据量的加倍，时间并没有增加多少，可以说基本是不增加的
print('binarySearch')
for i in range(10, 20):
    n = 2**i
    arr = TestData.generateOrderArray(size=n)
    start = time.time()
    TestProgram.binarySearch(arr, 1000)
    end = time.time()
    print('the number of data n =', n, 'the run time:',end-start)

#测试findMax，时间复杂度为O(n),可看到随着数据量的加倍，用的时间也加倍，即时间与数据量是呈正比的
print('findMax')
for i in range(10, 20):
    n = 2**i
    arr = TestData.generateRandomArray(size=n)
    start = time.time()
    TestProgram.findMax(arr)
    end = time.time()
    print('the number of data n =', n, 'the run time:',end-start)

#测试归并排序，mergeSort，其时间复杂度是O(nlogn)，随着数据量的加倍，用的时间也加倍，与O(n)的时间趋势大体相同
print('mergeSort')
for i in range(10, 20):
    n = 2**i
    arr = TestData.generateRandomArray(size=n)
    start = time.time()
    TestProgram.mergSort(arr)
    end = time.time()
    print('the number of data n =', n, 'the run time:',end-start)

#测试归并排序，selectionSort，其时间复杂度是O(n2),随着数据量成倍的增加，所用的时间是呈平方的增加的。
print('selectionSort')
for i in range(10, 20):
    n = 2**i
    arr = TestData.generateRandomArray(size=n)
    start = time.time()
    TestProgram.selectionSort(arr)
    end = time.time()
    print('the number of data n =', n, 'the run time:',end-start)



