import numpy as np

class TestData:

    @classmethod
    def generateRandomArray(cls,l=0, h=100000, size=10000):
        return list(np.random.randint(low = l, high= h, size=size))

    @classmethod
    def generateOrderArray(cls, l=0, h=100000, size = 100000):
        return list(np.linspace(l,h,size))



