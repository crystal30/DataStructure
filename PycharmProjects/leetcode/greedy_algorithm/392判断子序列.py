class Solution:
    def isSubsequence(self, s: str, t: str):
        len_s = len(s)
        len_t = len(t)

        si = 0
        ti = 0
        re = 0
        while si < len_s and ti < len_t:
            if t[ti] == s[si]:
                ti += 1
                si += 1
                re += 1
            else:
                ti += 1

        if re == len_s:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution()
    s = "axc"
    t = "ahbgdc"
    re = so.isSubsequence(s, t)
    print(re)
