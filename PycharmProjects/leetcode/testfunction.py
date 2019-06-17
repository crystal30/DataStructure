from TestTime import TestTime
from UsingArray.SortColors75 import Solution
import time

for i in range(15,25):
    size = 2 ** i
    nums = TestTime.notSortedArray(size=size)
    ll = set(nums)
    ll.add(1)
    # start = time.time()
    # nums.append(0)   #O（1）的时间复杂度
    # end = time.time()
    # print('size=',size, ' list append time=',end - start)

    # start = time.time()
    # nums.remove(nums[0])  # O（n）的时间复杂度
    # end = time.time()
    # print('size=', size, ' list remove time=', end - start)

    # start = time.time()
    # re = 10 in nums  #O(n)的时间复杂度,不太确定
    # end = time.time()
    # print('size=', size, ' list exits time=', end - start)

    # start = time.time()
    # ll.add(0)  # O(1)的时间复杂度
    # end = time.time()
    # print('size=', size, ' set add time=', end - start)

    start = time.time()
    re = 1 in ll  # O(1)的时间复杂度
    end = time.time()
    print('size=', size, ' set remove time=', end - start)

