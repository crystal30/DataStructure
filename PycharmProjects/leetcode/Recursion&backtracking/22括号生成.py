# 用copy（类似于48题的字符串排列）和不用copy（使用一个数组来标记是否被访问过），均超时
class Solution:
    def __init__(self):
        self.re = set()
        self.visited = None
        self.n = 0
    def generateParenthesis(self, n: int):
        if n == 1:
            return ["()"]
        if n == 2:
            return ["(())", "()()"]
        self.n = n
        s_list = list("()" * n)
        self.visited = [False for _ in range(2*n)]
        self._generate_parenthesis(s_list, "")
        return list(self.re)

    def _generate_parenthesis(self, s_list, sub_s):
        if len(sub_s) == self.n * 2 and self.is_valid(sub_s):
            self.re.add(sub_s)
            return
        for i in range(len(s_list)):
            if self.visited[i] is False:
                self.visited[i] = True
                self._generate_parenthesis(s_list, sub_s+s_list[i])
                self.visited[i] = False
        return

    def is_valid(self, s):
        len_s = len(s)
        if len_s <= 1:
            return False

        stack = [s[0]]
        for i in range(1, len_s):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(s[i])
        if len(stack) != 0:
            return False
        else:
            return True

# 但是这个我不是很明白
class Solution1:
    def __init__(self):
        self.ans = []
        self.n = 0
    def generateParenthesis(self, n: int):
        self.n = n
        self.generate([])
        return self.ans

    def generate(self, A):
        if len(A) == 2 * self.n:
            if self.valid(A):
                self.ans.append("".join(A))
            return

        A.append('(')
        self.generate(A)
        A.pop()
        A.append(')')
        self.generate(A)
        A.pop()
        return

    def valid(self, A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0



class Solution2:
    def __init__(self):
        self.ans = []
        self.n = 0
    def generateParenthesis(self, n: int):
        self.n = n
        self.backtrack([], 0, 0)
        return self.ans


    def backtrack(self, S, left, right):
        if len(S) == 2 * self.n:
            self.ans.append(''.join(S))
            return

        if left < n:
            S.append('(')
            self.backtrack(S, left+1, right)
            S.pop()
        if right < left:
            S.append(')')
            self.backtrack(S, left, right+1)
            S.pop()

if __name__ == "__main__":
    so = Solution2()
    n = 4
    re = so.generateParenthesis(n)
    print(re)
