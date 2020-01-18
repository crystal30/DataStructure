class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

    def twoSum1(self, numbers, target):
        n = len(numbers)
        for i in range(n-1):
            e = target - numbers[i]
            index = self.Binary_search(numbers, i+1, n-1, e)
            if index != None:
                return [i+1, index+1]

    def Binary_search(self, numbers, i, j, e):
        # 用二分查找法，在numbers[i,j]中查找元素e
        while i <= j:
            mid = i + (j-i)//2
            if numbers[mid] > e:
                j = mid - 1
            elif numbers[mid] < e:
                i = mid + 1
            else:
                return mid
        return None



if __name__ == "__main__":

    nums = [2, 7, 11, 15]
    target = 9

    so = Solution()
    re = so.twoSum1(nums, target)
    pass
