from copy import copy
class Solution:
    def __init__(self):
        self.re = []
    def partition(self, s: str):
        self.sub_partition(s, 0, [])
        return self.re

    def sub_partition(self, s, index, sub_par):
        len_s = len(s)

        if index == len_s:
            if sub_par != []:
                self.re.append(sub_par)
            return

        if self.is_palindrome(s[:index+1]) == True:
            temp = sub_par.copy()
            temp.append(s[:index + 1])
            self.sub_partition(s[index+1:], 0, temp)
        if len_s != 1 and s[index+1:] != '':
            self.sub_partition(s, index+1, sub_par)

        return

    def is_palindrome(self, s):
        i = 0
        j = len(s)-1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

class Solution1:
    def __init__(self):
        self.res = []
    def partition(self, s: str):
        if len(s) <= 1:
            return [[s]]
        self._par(s, [])
        return self.res

    def _par(self, s, sub_list):
        if s == '':
            self.res.append(copy(sub_list)) # 看这里需不需要加copy
            return

        len_s = len(s)
        for i in range(1, len_s+1):
            if self.is_palindrome(s[:i]):
                sub_list.append(s[:i])
                self._par(s[i:], sub_list)
                sub_list.pop()
            else:
                continue
        return

    def is_palindrome(self, sub_s):
        len_s = len(sub_s)
        i = 0
        j = len_s - 1
        while i <= j:
            if sub_s[i] != sub_s[j]:
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    so = Solution1()
    s = 'aab'
    re = so.partition(s)
    print(re)

