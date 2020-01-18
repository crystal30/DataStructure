class Solution:
    def maxArea(self, height):
        n = len(height)

        max_contain = 0
        l = 0
        r = n-1
        while l < r:
            if height[l] <= height[r]:
                contain = (r - l) * height[l]
                l += 1
            else:
                contain = (r - l) * height[r]
                r -= 1
            if contain > max_contain:
                max_contain = contain
        return max_contain

if __name__ == '__main__':
    so = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    re = so.maxArea(height)
    print(re)


