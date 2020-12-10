class Solution:
    def findContentChildren(self, g, s):
        len_g = len(g)
        len_s = len(s)

        s.sort()
        g.sort()
        if len_g >= len_s:
            satisfy_g = g[:len_s]
            satisfy_s = s
        else:
            satisfy_s = s[-len_g:]
            satisfy_g = g

        satisfy_len = min(len_s, len_g)
        satisfy_g_i = satisfy_len-1
        satisfy_s_i = satisfy_len-1
        re = 0
        while satisfy_g_i >=0 and satisfy_s_i >=0:
            if satisfy_g[satisfy_g_i] <= satisfy_s[satisfy_s_i]:
                re += 1
                satisfy_g_i -= 1
                satisfy_s_i -= 1
            else:
                satisfy_g_i -= 1

        return re


if __name__ == "__main__":
    so = Solution()
    g = [2,4,6,8]
    s = [1,2,3,9]
    re = so.findContentChildren(g, s)
    print(re)


