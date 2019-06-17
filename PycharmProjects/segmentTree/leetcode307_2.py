#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# AC 但是原理还有待搞明白
class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.arr = [0]*2*self.n
        self.build()

    def build(self):
        for i in range(self.n, self.n << 1):
            self.arr[i] = self.nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.arr[i] = self.arr[i << 1] + self.arr[i << 1 | 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += self.n
        self.arr[i] = val
        while i > 0:
            self.arr[i >> 1] = self.arr[i] + self.arr[i ^ 1]
            i >>= 1

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        i += self.n
        j += self.n
        while i <= j:
            if i & 1 == 1:
                res += self.arr[i]
                i += 1
            if j & 1 == 0:
                res += self.arr[j]
                j -= 1
            i >>= 1
            j >>= 1
        return res