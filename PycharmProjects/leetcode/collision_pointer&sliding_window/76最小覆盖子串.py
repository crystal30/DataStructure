class Solution:
    def minWindow(self, s: str, t: str) -> str:

        list_t = list(t)

        len_s = len(s)

        # 考虑len_s = 0 或 len_s = 1 的情况

        # len_s > 1的情况
        l = 0
        r = -1
        len_re = len_s + 1
        list_window = []
        while l < len_s:
            if r + 1< len_s:
                if s[r + 1] in t:
                    list_window.append(s[r+1])
                r += 1
            else:
                if s[l] in t:
                    list_window.remove(s[l])
                    l += 1
                if s[r] not in t:
                    r -= 1

            while l < len_s and s[l] not in t:
                l += 1

            while set(list_t) == set(list_window) and len(list_window) >= len(list_t):
                if len(list_t) == len(list_window):
                    if r - l + 1 < len_re:
                        re = s[l:r + 1]
                        len_re = len(re)
                        if s[l] in list_window:
                            list_window.remove(s[l])
                        l += 1
                    else:
                        if s[l] in list_window:
                            list_window.remove(s[l])
                        l += 1
                elif len(list_window) > len(list_t):
                    if s[l] in t:
                        list_window.remove(s[l])
                    l += 1


        if len_re == len_s + 1:
            return ''
        else:
            return re

if __name__ == "__main__":
    so = Solution()
    s = "cabwefgewcwaefgcf"
    t = "cae"
    re = so.minWindow(s, t)
    print(re)








