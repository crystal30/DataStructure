from collections import Counter
class Solution:
    #滑动窗口，
    #316ms
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dd = {}
        temp = {}
        for k in t:
            if k not in dd:
                dd[k] = 1
            else:
                dd[k] += 1
        count = len(t)
        #滑动窗口
        i = 0
        j = -1
        re_n = len(s)+1
        while i < len(s):
            if s[i] in dd:
                for k in temp:
                    if temp[k] !=0 and dd[k] != 0:
                        dd[k] -= 1
                        count -= 1
                        temp[k] += 1
                if j+1 == len(s) and count !=0:
                        break
                while j+1 < len(s) and count !=0:
                    if s[j+1] in dd:
                        if dd[s[j+1]] == 0:
                            if s[j+1] not in temp:
                                temp[s[j+1]] = -1
                            else:
                                temp[s[j + 1]] -= 1
                        else: #dd[s[j+1]] != 0
                            dd[s[j+1]] -= 1
                            count -= 1
                    j += 1
            else:
                while i+1 < len(s) and s[i+1] not in dd:
                    i += 1
                i += 1
            if count == 0:
                if re_n > j-i+1:
                    re_n = j -i +1
                    re = s[i:j+1]
                dd[s[i]] += 1
                count += 1
                i += 1
        return "" if re_n == len(s)+1 else re

    #改进minWindow,多定义了一个windows_dd = {}，windows_count = 0，这两个变量，
    # 使得代码的操作更简单，用时更短
    #156ms
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dd = Counter(t)
        t_count = len(t_dd)
        re_n = len(s)+1
        #滑动窗口s[i,j],初始窗口s[0,-1]无效
        i = 0
        j = -1
        windows_dd = {}
        windows_count = 0
        while j+1<len(s):
            c = s[j+1]
            windows_dd[c] = windows_dd.get(c,0)+1
            if c in t_dd and windows_dd[c] == t_dd[c]:
                windows_count += 1
            j += 1
            while windows_count == t_count:
                if j-i+1 < re_n:
                    re_n = j-i+1
                    re = s[i:j+1]
                ic = s[i]
                windows_dd[ic] = windows_dd.get(ic,0)-1
                if ic in t_dd and windows_dd[ic] < t_dd[ic]:
                    windows_count -= 1
                i += 1
        return "" if re_n == len(s)+1 else re

if __name__ == "__main__":
    S = "ABAACBAB"
    T = "ABC"
    so = Solution()
    re = so.minWindow1(S,T)
    pass

