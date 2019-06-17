#"pwwkew"
class Solution(object):
    # 使用滑动窗口
    # 72ms
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #考虑空字符串的情况
        n = len(s)
        if n == 0:
            return 0
        i,j, res = 0, -1, 0
        while i <n:
            while j+1<n and s[j+1] not in s[i:j+1]:
                j += 1
            res = max(res, j+1-i)
            j += 1
            while j<n and i < j and s[i] != s[j]:
                i += 1
            i += 1
        return res

    #滑动窗口，假设s[l,r]存储的为最长的字符串，
    # 初始空窗口l = 0, r = -1；结束空窗口l=len(s),r = len(s)-1
    #96 ms
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = -1
        res = 0
        freq = [0]*128
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:# r+1>=len(s) or freq[ord(s[r+1])] == 1
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r + 1 - l)
        return res

    #对lengthOfLongestSubstring2的结束窗口进行改进
    def lengthOfLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = -1
        res = 0
        freq = [0]*128
        while l < len(s):
            if r + 1 < len(s) and freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:# freq[ord(s[r+1])] == 1 #r+1>=len(s) 已经不会进入此条判断，而是直接进入下边的if语句
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r + 1 - l)
            #改进，不用等到结束空窗口l=len(s),r = len(s)-1时才结束，
            #在r == len(s)-1的时候就可以结束，因为此时每次都是l += 1,字符串的长度只会比原来更小
            if r == len(s)-1:
                break
        return res

    #对lengthOfLongestSubstring4的结束窗口进行改进，只是和lengthOfLongestSubstring3的写法不同而已
    def lengthOfLongestSubstring4(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = -1
        res = 0
        freq = [0]*128
        while r+1 < len(s):
            if freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:# freq[ord(s[r+1])] == 1 #r+1>=len(s) 已经不会进入此条判断，而是直接进入下边的if语句
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r + 1 - l)
        return res


    # lengthOfLongestSubstring4的另一种写法
    def lengthOfLongestSubstring5(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = -1
        res = 0
        freq = [0]*128
        while l < len(s):
            if r+1 < len(s) and freq[ord(s[r+1])] == 0:
                r += 1
                freq[ord(s[r])] += 1
            else:# freq[ord(s[r+1])] == 1 #r+1>=len(s) 已经不会进入此条判断，而是直接进入下边的if语句
                freq[ord(s[l])] -= 1
                l += 1
            res = max(res, r + 1 - l)
        return res

if __name__ == "__main__":
    s = " "
    so = Solution()
    res = so.lengthOfLongestSubstring4(s)
    pass








