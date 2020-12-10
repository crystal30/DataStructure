# encoding:utf-8
# 用暴力破解的方法，超时
class Solution:
    def longestPalindrome(self, s: str):
        len_s = len(s)
        if len_s <= 1:
            return s

        max_len = 0
        left = 0
        right = 0
        for i in range(len_s):
            for j in range(len_s, i, -1):
                if max_len < j-i and self.__is_palindrome(s, i, j):
                    left = i
                    right = j
                    max_len = j - i
                    break

        return s[left:right]

    def __is_palindrome(self, s, i, j):
        len_s = j - i
        if len_s == 1:
            return True
        mid = i + len_s // 2
        for k in range(i, mid):
            if s[k] != s[j-(1+k-i)]:
                return False
        return True


# 用滑动窗口,超时
class Solution1:
    def longestPalindrome(self, s: str):
        len_s = len(s)
        if len_s <= 1:
            return s

        re = ''
        for i in range(len_s):
            for j in range(i+1, len_s+1):
                sub_s = s[i:j]
                if j-i > len(re) and self.__is_palindrome(sub_s, i, j):
                    re = sub_s

        return re


    def __is_palindrome(self, s, i, j):
        len_s = j-i
        if j-i == 1:
            return True
        div = len_s // 2
        mod = len_s % 2
        sub_s_1 = s[:div]
        sub_s_2 = s[div+mod:]
        if sub_s_1 == sub_s_2[::-1]:
            return True
        else:
            return False

# 用动态规划
class Solution3:
    def longestPalindrome(self, s: str):
        len_s = len(s)
        if len_s <= 1:
            return s

        # memo[i][j]=True 表示s[i][j](前闭后闭)是回文串，否则表示不是回文串
        memo = [[False for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s):
            memo[i][i] = True

        max_len = 1
        left = 0
        right = 0
        for i in range(len_s-1,-1,-1):
            for j in range(i+1, len_s):
                if s[i] == s[j]:
                    if j-i >= 3 and memo[i+1][j-1] is not True:
                        memo[i][j] = False
                    else:
                        memo[i][j] = True
                        if j - i + 1 > max_len:
                            left = i
                            right = j
                            max_len = j - i + 1
                else:
                    memo[i][j] = False

        return s[left:right+1]


if __name__ == "__main__":
    s = "baab"
    so = Solution3()
    re = so.longestPalindrome(s)
    print(re)

