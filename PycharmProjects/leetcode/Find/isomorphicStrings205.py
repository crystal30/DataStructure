class Solution:
    #此道题目类似与290题
    #用两个字典来实现
    #88ms
    #时间复杂度：O(len(s))
    #空间复杂度O(len(s))
    #字典是由哈希实现的，增删改查的复杂度均为O(1)
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dd_s = {}
        dd_t = {}
        for i in range(len(s)):
            if s[i] not in dd_s and t[i] not in dd_t:
                dd_s[s[i]] = t[i]
                dd_t[t[i]] = s[i]
            elif s[i] in dd_s:
                if dd_s[s[i]] != t[i]:
                    return False
            elif t[i] in dd_t:
                if dd_t[t[i]] != s[i]:
                    return False
        return True

    #用两个列表来实现
    #188ms
    #用列表比用字典慢一些，感觉列表的查询操作是O(n),因为其要遍历一遍数组
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d_s = []
        d_t = []
        for i in range(len(s)):
            if s[i] not in d_s and t[i] not in d_t:
                d_s.append(s[i])
                d_t.append(t[i])
            elif s[i] in d_s:
                if d_t[d_s.index(s[i])] != t[i]:
                    return False
            elif t[i] in d_t:
                if d_s[d_t.index(t[i])] != s[i]:
                    return False
        return True

    #同样用290题的思路，并且此时两个字符串的长度是相等的，相比较290来说更加简单
    #56 ms
    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dd_s = {}
        dd_t = {}
        for i in range(len(s)):
            if dd_s.get(s[i],0) != dd_t.get(t[i],0):
                return False
            dd_s[s[i]] = dd_t[t[i]] = i+1
        return True

if __name__ == "__main__":
    s = "egg"
    t = "add"

