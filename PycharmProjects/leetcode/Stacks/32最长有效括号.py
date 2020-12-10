# 用栈的方式
class Solution:
    def longestValidParentheses(self, s: str):
        len_s = len(s)
        if len_s <= 1:
            return 0

        stack = []
        for index, sub_s in enumerate(s):
            if len(stack) != 0 and (s[stack[-1]] == "(" and sub_s == ")"):
                stack.pop()
            else:
                stack.append(index)

        len_stack = len(stack)
        if len_stack == 0:
            return len_s
        else:
            re = [stack[0], len_s - stack[-1] - 1]
            for i in range(0, len_stack-1):
                re.append(stack[i+1] - stack[i] - 1)
            return max(re)


if __name__ == "__main__":
    so = Solution()
    # s = "(())((((())))))))((()"
    s = ")()())"
    re = so.longestValidParentheses(s)
    print(re)