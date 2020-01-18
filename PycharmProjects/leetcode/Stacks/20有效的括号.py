class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            if e in '{[(':
                stack.append(e)
            else: # e in '}])'
                if stack == []:
                    return False
                elif e == ')' and stack.pop() != '(':
                    return False
                elif e == '}' and stack.pop() != '{':
                    return False
                elif e == ']' and stack.pop() != '[':
                    return False

        if stack == []:
            return True
        else:
            return False

if __name__ == "__main__":
    so = Solution()
    s = '()'
    re = so.isValid(s)
    print(re)
