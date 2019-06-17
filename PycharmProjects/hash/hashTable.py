# -*- coding: utf-8 -*-

class HashTable():
    def __init__(self, M=97):
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

    def remove(self, key):
        map = self.hashTable[self.__hash(key)]
        assert key in map, "key must be in map"
        del map[key]

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
if __name__ == '__main__':
    import numpy as np
    nums = np.random.normal(loc=0.0, scale=1.0, size=100000)
    ht = HashTable()
    for num in nums:
        ht.add(num,100)












