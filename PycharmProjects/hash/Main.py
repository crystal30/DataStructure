from hashTable import HashTable
from hashTable1 import HashTable as HT
from AVLMap import AVLMap

import numpy as np
import datetime

# nums = np.random.normal(loc=0.0, scale=1.0, size=100000)
nums = [3,2,4,7,8,91,1,5,6]*100

start = datetime.datetime.now()
ht = HT()
for num in nums:
    if ht.contains(num):
        ht.set(num, ht.get(num)+1)
    else:
        ht.add(num,1)
for num in set(nums):
    print(ht.get(num))

end = datetime.datetime.now()
print(end-start)


start = datetime.datetime.now()
ht = HashTable()
for num in nums:
    if ht.contains(num):
        ht.set(num, ht.get(num)+1)
    else:
        ht.add(num,1)
for num in set(nums):
    print(ht.get(num))

end = datetime.datetime.now()
print(end-start)

start = datetime.datetime.now()
avl = AVLMap()
for num in nums:
    if avl.contains(num):
        avl.set(num, avl.get(num)+1)
    else:
        avl.add(num,1)
for num in set(nums):
    print(avl.get(num))
end = datetime.datetime.now()
print(end-start)
