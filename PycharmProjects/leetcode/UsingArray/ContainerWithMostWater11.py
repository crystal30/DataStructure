class Solution(object):
    #暴力破解，两遍遍历
    #时间复杂度O（n2）

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mArea = 0
        for i in range(n-1):
            for j in range(i+1, n):
                newArea = (j - i)*min(height[i], height[j])
                mArea = max(mArea, newArea)
        return mArea

    # Time Limit Exceeded
    # 指针对撞l，r，初始化为l = 0， r= len(height)-1
    # 时间复杂度为O（n2）
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mArea = 0
        l = 0
        r = n - 1
        while l < r:
            i = l
            m = l  # m中存放元素值最大的那个下标
            #此时r不变
            while i < r:
                newArea = min(height[r],height[m]) * (r-m)
                mArea = max(mArea, newArea)
                if height[i+1] > height[m]:
                    m = i+1
                    i += 1
                elif height[i+1] <= height[m]:
                    i += 1
            #此时量不变，j从r依次向前遍历
            j = r
            m = j
            while j > l:
                newArea = min(height[l],height[m]) * (m - l)
                if newArea > mArea:
                    mArea = newArea
                if height[j-1] > height[m]:
                    m = j-1
                    j -= 1
                elif height[j-1] <= height[m]:
                    j -= 1
            l += 1
            r -= 1
        return mArea

    #对撞指针2
    #时间复杂度为O（n）
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        mArea = min(height[i],height[j])*(j-i)
        while i<j:
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            mArea = max(mArea, min(height[i],height[j])*(j-i))
        return mArea
if __name__ == "__main__":
    height = [2,3,4,5,18,17,6]
    so = Solution()
    re = so.maxArea2(height)
    pass

