import sort
import datetime
import numpy as np
import random
size = 1000000
nums = list(np.linspace(0,1000,size))
for i in range(100):
    i = random.randint(0,size-5)
    nums[i], nums[i+5] = nums[i+5], nums[i]

def isSorted(Sortedarr):
    for i in range(size-1):
        if Sortedarr[i] > Sortedarr[i+1]:
            return False
    return True
def testSort(sortClassName,nums):
    start = datetime.datetime.now()
    sorted_data = sortClassName(nums)
    end = datetime.datetime.now()
    assert isSorted(sorted_data), "Sorting error"
    print("{} run time: {}".format(str(sortClassName), end-start))
#
# testSort(sort.Sort.selectionSort,nums)
# testSort(sort.Sort.improveInsertionSort,nums)
# testSort(sort.Sort.insertionSort,nums)
# testSort(sort.Sort.improveBubbleSort,nums)
# testSort(sort.Sort.bubbleSort,nums)
# testSort(sort.Sort.improveBubbleSort,nums)
# testSort(sort.Sort.shellSort,nums)

testSort(sort.Sort.MergeSort,nums)
testSort(sort.Sort.quickSort,nums)
testSort(sort.Sort.quickSort2,nums)


