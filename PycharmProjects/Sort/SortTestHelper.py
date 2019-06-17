import sort
import numpy as np
import datetime
import random
from  Student import Student
from copy import copy
from ttQuickSort import QuickSort
class SortTestHelper():
    def __init__(self,size=100,low=10,high=200):
        self.size = size
        self.nums = list(np.random.randint(low=low,high=high,size=size))
    #判断arr数组是否有序
    def isSorted(self, Sortedarr):
        # print(Sortedarr)
        # print(self.size)
        for i in range(self.size - 1):
            if Sortedarr[i] > Sortedarr[i+1]:
                return False
        return True

    # 测试sortClassName所对应的排序算法排序arr数组所得到结果的正确性和算法运行时间
    def testSort(self, sortClassName):
        start = datetime.datetime.now()
        nums = copy(self.nums)
        sorted_data = sortClassName(nums)
        end = datetime.datetime.now()
        # print(self.nums == sorted_data)
        # print(sorted_data)
        # print(self.nums)
        assert self.isSorted(sorted_data), "Sorting error"
        print("{} run time: {}".format(str(sortClassName), end-start))

class  SortTestNearlyOrderly(SortTestHelper):
    def __init__(self, size=100, change= 10):
        SortTestHelper.__init__(self,size)
        self.nums = list(np.linspace(0, 1000, self.size))
        for i in range(change):
            i = random.randint(0, self.size-5)
            self.nums[i], self.nums[i+5] = self.nums[i+5], self.nums[i]



if __name__ == "__main__":
    #随机数组排序
    print('随机数组排序')
    for i in range(10,20):
        Test = SortTestHelper(size=2**i, low = 1, high=100)
        Test.testSort(QuickSort.sort4)


    # print('近乎有序的数组排序')
    # #近乎有序的数组排序
    # Test1 = SortTestNearlyOrderly(size=10000,change=20)
    # Test1.testSort(sort.Sort.MergeSort)
    #
    # print('对于重复元素较多的数组')
    # Test = SortTestHelper(size=1000, low=1, high=10)
    # Test.testSort(sort.Sort.MergeSort)
