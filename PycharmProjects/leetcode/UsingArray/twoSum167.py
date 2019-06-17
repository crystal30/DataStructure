class Solution(object):
    #循环的次数为(n-1) + (n-2) + (n-3)+.....+1 = 1/2*n(n-1),故时间复杂度为O(n2)
    #空间复杂度为O(1)
    # Time Limit Exceeded
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n-1):
            for j in range(i+1, n):
                if numbers[i] + numbers[j] == target:
                    return i+1, j+1
                if numbers[i] + numbers[j] > target:
                    break
    #定位numbers[i], 用二分搜索法看numbers[i+1, n-1]中是否有元素 == target-numbers[i]，
    # 其中n为numbers数组的长度
    #84ms 二分搜索法用递归的写法
    #56 ms 二分搜索法用非递归的写法
    #时间复杂度O(nlogn)
    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n-1):
            e = target - numbers[i]
            index = self.binarySearch1(numbers, i+1, n-1, e)
            if index == -1:
                continue
            else:
                return i+1, index+1

    #二分搜索法的搜寻范围numbers[l,r],若该范围中包含要搜寻的元素e，返回其index(这里的index是从0开始的)
    #若该范围中不包含要搜索的元素e，返回-1
    #时间复杂度  O(logn)
    def binarySearch(self, numbers, l, r, e):
        if l>r:
            return -1

        mid = l + (r-l)//2
        if e > numbers[mid]:
            return self.binarySearch(numbers, mid+1, r, e)
        if e < numbers[mid]:
            return self.binarySearch(numbers, l, mid-1, e)
        if e == numbers[mid]:
            return mid

    #二分搜索法非递归的写法
    def binarySearch1(self, numbers, l, r, e):
        assert l>0 and l<len(numbers), "l is invalid"
        assert r>0 and r<len(numbers), "r is invalid"
        while l <= r:
            mid = l + (r-l)//2
            if e > numbers[mid]:
                l = mid+1
            elif e < numbers[mid]:
                r = mid-1
            else: #e == numbers[mid]
                return mid
        return -1


    #对撞指针
    #时间复杂度O(n)
    #24 ms
    def twoSum3(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers)-1
        while(l <r):
            if numbers[l] + numbers[r] == target:
                return l+1, r+1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: #numbers[l] + numbers[r] < target
                l += 1







if __name__ == '__main__':
    numbers = [-1, 0]
    so = Solution()
    i,j = so.twoSum3(numbers, -1)
    pass
