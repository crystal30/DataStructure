# -*- coding: utf-8 -*-

upperTol = 10 #平均每个地址所承载的元素的上限，一旦触碰，扩容
lowerTol = 2  #平均每个地址所承载元素的下限，一旦触碰，缩容
initCapacity = 7 # 初始的地址的容量
class HashTable():

    def __init__(self, M=initCapacity):
        self.M= M
        self.size = 0
        self.hashTable = dict()
        for i in range(M):
            self.hashTable[i] = dict()

    #计算出每个键值对应的索引（0.....M-1）,每个索引背后又对应一个字典
    def __hash(self,key):
        return (hash(key) & 0x0fffffff) % self.M

    def getSize(self):
        return self.size

    def add(self, key, value):

        map = self.hashTable[self.__hash(key)]
        if key not in map:
            map[key] = value
            self.size += 1
        else:
            map[key] = value
        if self.M * upperTol >= self.size:
            self.__resize(self.M*2)

    def remove(self, key):
        map = self.hashTable[self.__hash(key)]
        assert key in map, "key must be in map"
        del map[key]
        self.size -= 1
        if self.M *lowerTol <= self.size and self.M//2 >= initCapacity:
            self.__resize(self.M//2)

    def set(self, key, value):
        map = self.hashTable[self.__hash(key)]
        assert key in map, "key must be in map"
        map[key] = value

    def contains(self,key):
        map = self.hashTable[self.__hash(key)]
        if key in map:
            return True
        else:
            return False

    def get(self, key):
        map = self.hashTable[self.__hash(key)]
        if key in map:
            return map[key]
        else:
            return None

    def __resize(self, newM):
        ht = dict()
        for i in range(newM):
            ht[i] = dict()
        self.M = newM
        for map in self.hashTable.values():
            for key in map:
                newMap = ht[self.__hash(key)]
                if key not in newMap:
                    newMap[key] = map[key]

        self.hashTable = ht

if __name__ == '__main__':
    import numpy as np
    nums = np.random.normal(loc=0.0, scale=1.0, size=100000)
    ht = HashTable()
    for num in nums:
        ht.add(num,100)












