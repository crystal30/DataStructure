from copy import copy
class Solution(object):
    # Time Limit Exceeded
    #时间复杂度O(m*n)
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq = [0]*26
        n = len(p)
        m = len(s)
        res = []
        #时间复杂度，O(n)
        for k in p:
            freq[ord(k)-ord('a')] += 1
        l = 0
        #时间复杂度O(m*n)
        while l < m-n+1:
            i = l
            freq_copy = copy(freq)
            while i < m and freq_copy[ord(s[i])-ord('a')] != 0:
                freq_copy[ord(s[i]) - ord('a')] -= 1
                i += 1
            if i-l == n:
               res.append(l)
            l += 1
        return res

    #虽然做了改进，但是仍然超时
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq = [0]*26
        n = len(p)
        m = len(s)
        res = []
        #时间复杂度，O(n)
        for k in p:
            freq[ord(k)-ord('a')] += 1
        l = 0
        #时间复杂度O(m*n)
        while l < m-n+1:
            i = l
            freq_copy = copy(freq)
            while i < m and freq_copy[ord(s[i])-ord('a')] != 0:
                freq_copy[ord(s[i]) - ord('a')] -= 1
                i += 1
            if i-l == n:
                res.append(l)
            #对l的赋值进行改进
            if i < m and s[i] not in p:
                l = i+1
            else:
                l += 1
        return res

    #d.fromkeys(l, 0)
    #滑动窗口
    #360ms ,改进？
    #时间复杂度O（n），但是中间的操作可能比较繁琐
    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq = [0]*26
        for k in p:
            freq[ord(k)-ord('a')] += 1
        count = len(p)
        #滑动窗口，i，j,  s[i,j]
        i = 0
        j = -1
        res = []
        while i <= len(s)-len(p):
            while j+1 < len(s) and freq[ord(s[j+1]) - ord('a')] != 0:
                j += 1
                freq[ord(s[j]) - ord('a')] -= 1
                count -= 1
            if count == 0:
                res.append(i)
                freq[ord(s[i]) - ord('a')] += 1
                count += 1
                i += 1
            else:
                if j+1<len(s) and s[j+1] in p:
                    freq[ord(s[i]) - ord('a')] += 1
                    count += 1
                    i += 1
                else: #j+1>=len(s) or s[j+1] not in p
                    if j+1>=len(s):
                        break
                    else:
                        for _ in range(i, j + 1):
                            freq[ord(s[_]) - ord('a')] += 1
                            count += 1
                        j += 1
                        i = j+1
        return res


if __name__ == "__main__":
    # s="cbaebabacd"
    # p="abc"
    # [0, 6]
    s="abab"
    p="ab"
    #[0, 1, 2]
    so = Solution()
    re = so.findAnagrams2(s,p)
    print(re)






