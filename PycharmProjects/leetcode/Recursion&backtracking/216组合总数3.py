from copy import copy
class Solution:
    def __init__(self):
        self.res = []
    def combinationSum3(self, k: int, n: int):
        visited = [False] * 10
        self._combination_sum(k, n, 1, visited, [])
        return self.res

    def _combination_sum(self, k, n, start, visited, sub_re):
        if k == len(sub_re):
            if n == 0:
                self.res.append(copy(sub_re))
            return

        for i in range(start, 10):
            if n < i:
                break
            if visited[i] == False:
                visited[i] = True
                sub_re.append(i)
                n -= i
                self._combination_sum(k, n, i+1, visited, sub_re)
                n += sub_re.pop()
                visited[i] = False
        return

if __name__ == "__main__":
    so = Solution()
    k = 3
    n = 7
    re = so.combinationSum3(k, n)
    print(re)


