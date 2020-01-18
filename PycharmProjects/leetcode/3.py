class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = -1 # s[l,r] 存储的为不含有重复字符的子串
        sub_s = ''
        re = 0

        if n == 1:
            # 当字符串长度为1时
            pass
        while l < n:
            if r + 1 < n and s[r + 1] not in sub_s:
                r += 1
            else:
                l += 1

            sub_s = s[l: r+1]
            if len(sub_s) > re:
                re = len(sub_s)

        if re == 0:
            return 0
        return re

    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
        # 字符为空；字符长度为1
        freq = [0] * 256
        re = 0
        l = 0
        r = -1
        while l < n:
            if r+1 < n and freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:
                freq[ord(s[l])] -= 1
                l += 1

            re = max(re, r - l + 1)

        return re


if __name__ == "__main__":
    so = Solution()
    s = "abcabcbb"
    re = so.lengthOfLongestSubstring1(s)
    print(re)
