class Solution:
    def simplifyPath(self, path: str) -> str:
        len_path = len(path)
        if len_path <= 1:  # path 会不会为'a' '.'等？
            return path

        stack = [path[0]]
        for i in range(1, len_path):
            if path[i] == "/":
                if stack[-1] == '.' and stack[-2] != '.':
                    stack.pop()
                elif stack[-2:] == ['.','.']: # stack[-2:] 验证一下
                    stack.pop() # 删除 '.'
                    stack.pop() # 删除 '.'
                    if stack == ['/']:
                        continue
                    stack.pop() # 删除 '/'
                    while stack[-1] != '/': # 知道删除到'/'结束 eg:/a/..
                        stack.pop()
                elif stack[-1] != '.' and stack[-1] != '/':
                    stack.append('/')
                # stack[-1] != '/' 不做任何操作

            else:
                stack.append(path[i])

        if stack[-1] == '.' and stack[-2] != '.':
            stack.pop()
        elif stack[-2:] == ['.', '.']:  # stack[-2:] 验证一下
            stack.pop()  # 删除 '.'
            stack.pop()  # 删除 '.'
            if stack != ['/']:
                stack.pop()  # 删除 '/'
                while stack[-1] != '/':  # 知道删除到'/'结束 eg:/a/..
                    stack.pop()

        if stack[-1] == '/' and len(stack) != 1:
            stack.pop()

        return ''.join(stack)

    def simplifyPath1(self, path: str) -> str:
        path_list = path.split('/') # 考虑 path = '/' '////' '。' 'a'

        stack = []
        for e in path_list:
            if e == '.' or e == '/' or e == '':
                pass
            elif e == '..':
                if stack != []:
                    stack.pop()
            else:
                stack.append(e)

        return '/'+'/'.join(stack)

if __name__ == '__main__':
    so = Solution()
    path = "/..."
    re = so.simplifyPath1(path)
    print(re)




