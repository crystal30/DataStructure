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

if __name__ == "__main__":
    so = Solution()
    s = 'aab'
    print(so.partition(s))
