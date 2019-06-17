from collections import Counter
class Solution:
    #52 ms
    #时间复杂度 O(len(s_dd))
    #空间复杂度 O(len(s_dd)+len(t_dd))
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dd = Counter(s)
        t_dd = Counter(t)
        t_count = len(t_dd)
        for k in s_dd:
            if k not in t_dd or t_dd[k] != s_dd[k]:
                return False
            else: # k in t_dd and t_dd[k] != s_dd[k]:
                t_count -= 1

        if t_count == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    so = Solution()
    re = so.isAnagram(s,t)
    pass

