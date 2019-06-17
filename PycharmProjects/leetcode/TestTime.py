import numpy as np

class TestTime:

    @classmethod
    def DuplicatesInSortedArray(cls, size = 1000):
        arr = []
        for i in range(size//2):
            arr.append(i)
            arr.append(i)
        return arr

    @classmethod
    def notSortedArray(cls, low = 1, high = 1000, size = 1000):
        return list(np.random.randint(low, high, size))



