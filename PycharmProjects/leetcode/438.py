from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):

        s_len = len(s)
        p_len = len(p)

        re = []

        freq_p = [0] * 26
        for e in p:
            freq_p[ord(e)-97] += 1

        l = 0
        r = -1
        freq_sub_s = [0] * 26
        while r + 1 < s_len:
            if s[r + 1] in p:
                r += 1
                freq_sub_s[ord(s[r])-97] += 1
            else:
                r += 1
                l = r + 1
                freq_sub_s = [0] * 26

            if freq_sub_s == freq_p:
                re.append(l)
                freq_sub_s[ord(s[l]) - 97] -= 1
                l += 1

            else:
                if r - l + 1 == p_len:
                    freq_sub_s[ord(s[l])-97] -= 1
                    l += 1
        return re

if __name__ == "__main__":
    so = Solution()
    s = "baa"
    p = "aa"
    re = so.findAnagrams(s, p)
    print(re)











