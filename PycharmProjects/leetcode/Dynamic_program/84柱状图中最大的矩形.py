# 动态规划，最后几个用例超时
class Solution:
    def largestRectangleArea(self, heights):
        len_heights = len(heights)
        if len_heights == 0:
            return 0

        if len_heights == 1:
            return heights[0]

        memo_heights = [[(-1,-1) for _ in range(len_heights)] for _ in range(len_heights)]
        for i in range(len_heights):
            memo_heights[i][i] = (heights[i],1)

        max_heights = max(heights)
        for i in range(len_heights-1, -1, -1):
            for j in range(i+1, len_heights):
                min_height = min(heights[i], memo_heights[i+1][j][0])
                len_height = memo_heights[i+1][j][1] + 1
                memo_heights[i][j] = (min_height, len_height)
                max_heights = max(max_heights, min_height * len_height)


        return max_heights


# 暴力破解 超时间
class Solution1:
    def largestRectangleArea(self, heights):
        len_heights = len(heights)
        if len_heights == 0:
            return 0
        if len_heights == 1:
            return heights[0]

        height_square = [-1 for _ in range(len_heights)]
        for index, height in enumerate(heights):
            len_height = 1
            for left in range(index-1, -1, -1):
                if heights[left] >= height:
                    len_height += 1
                else:
                    break

            for right in range(index+1, len_heights):
                if heights[right] >= height:
                    len_height += 1
                else:
                    break
            height_square[index] = height * len_height

        return max(height_square)


# 用数据栈
class Solution2:
    def largestRectangleArea(self, heights):
        len_heights = len(heights)
        if len_heights == 0:
            return 0
        if len_heights == 1:
            return heights[0]

        height_square = [-1 for _ in range(len_heights)]
        stack = []
        for index in range(len_heights):
            while len(stack) > 0 and heights[index] < heights[stack[-1]]:
                pre_index = stack.pop()
                if len(stack) == 0:
                    height_square[pre_index] = heights[pre_index] * (index)
                else:
                    height_square[pre_index] = heights[pre_index] * (index-stack[-1]-1)

            stack.append(index)

        while len(stack) > 0:
            pre_index = stack.pop()
            if len(stack) == 0:
                height_square[pre_index] = heights[pre_index] * (len_heights)
            else:
                height_square[pre_index] = heights[pre_index] * (len_heights - stack[-1] - 1)

        return max(height_square)


if __name__ == "__main__":
    so = Solution2()
    heights = [3,6,5,7,4,8,1,0]
    re = so.largestRectangleArea(heights)
    print(re)





