# AC
class NumArray:

    def __init__(self, nums):
        self.__n = len(nums)
        self.__tree = [None] * self.__n*4
        self.__subTree(0,0,self.__n-1,nums)

    def __subTree(self,ti,l,r,nums):
        if l==r:
            self.__tree[ti] = nums[l]
            return
        elif l<r:
            mid = l + (r-l)//2
            self.__subTree(ti*2+1,l,mid,nums)
            self.__subTree(ti*2+2, mid+1, r,nums)
            self.__tree[ti] = self.__tree[ti*2+1] + self.__tree[ti*2 + 2]
    def update(self, i, val):
        self.__set(i,val,0,0,self.__n-1)
    def __set(self,i,val,ti,l,r):
        if l == r:
            self.__tree[ti] = val
            return
        mid = l + (r-l)//2
        if i<=mid:
            self.__set(i,val,ti*2+1,l,mid)
        if i>= mid+1:
            self.__set(i, val, ti * 2 + 2, mid+1, r)
        self.__tree[ti] = self.__tree[ti*2+1] + self.__tree[ti*2 + 2]

    def sumRange(self, i, j):

        return self.__sum(i,j,0,0,self.__n-1)

    def __sum(self,i,j,ti,l,r):
        if i<=l and j>=r:
            return self.__tree[ti]
        if i>r or j<l:
            return 0
        mid = l + (r-l)//2
        return self.__sum(i,j,ti*2+1,l,mid) + self.__sum(i,j,ti*2+2,mid+1,r)

# ["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
# [[[0,9,5,7,3]],1[4,4],2[2,4],3[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
if __name__ == '__main__':
    nums = [0,9,5,7,3]
    so = NumArray(nums)
    re = so.sumRange(4,4)
    print(re)
    re = so.sumRange(2, 4)
    print(re)
    re = so.sumRange(3, 3)
    print(re)
    so.update(4,5)
    so.update(1,7)
    so.update(0,8)
    re = so.sumRange(1,2)
    print(re)
    so.update(1, 9)
    re = so.sumRange(4, 4)
    print(re)
    so.update(3, 4)
