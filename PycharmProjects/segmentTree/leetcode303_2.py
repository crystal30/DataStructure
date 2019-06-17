class NumArray:

    def __init__(self, nums):
        self.__n = len(nums)
        self.__tree = [0]*self.__n*4
        self.__subTree(nums, 0, 0, self.__n - 1)

    def __subTree(self, nums,index, l, r):
        if l == r:
            self.__tree[index] = nums[l]
        elif l<r:  # l<r
            mid = l + (r - l)// 2
            # lChild = index *2 +1
            # rChild = index*2 + 2
            self.__subTree(nums,index *2 +1, l, mid)
            self.__subTree(nums,index*2 + 2, mid + 1, r)
            self.__tree[index] = self.__tree[index*2 + 1] + self.__tree[index*2 + 2]


    def sumRange(self, i, j):
        return self.__query(0,0,self.__n-1, i,j)

    def __query(self,treeIndex, l, r, ql, qr):
        if ql<=l and r <= qr:
            return self.__tree[treeIndex]
        if ql >r or qr < l:
            return 0
        # leftChild = treeIndex * 2 +1
        # rightChild = treeIndex * 2 +2
        mid = l+(r-l)// 2
        return self.__query(treeIndex * 2 +1,l,mid,ql, qr) + self.__query(treeIndex * 2 +2, mid+1, r, ql, qr)

