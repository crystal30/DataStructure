class Solution:
    #56 ms
    #改进？
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dd1 = {}
        dd2 = {}
        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dd1 and str_list[i] not in dd2:
                dd1[pattern[i]] = str_list[i]
                dd2[str_list[i]] = pattern[i]
            elif pattern[i] in dd1 and dd1[pattern[i]] != str_list[i]:
                return False
            elif str_list[i] in dd2 and dd2[str_list[i]] != pattern[i]:
                return False
        return True

    #改进，用两个列表代替字典
    #52ms
    def wordPattern1(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ")
        if len(str_list) != len(pattern):
            return False
        d1 = []
        d2 = []
        for i in range(len(pattern)):
            if pattern[i] not in d1 and str_list[i] not in d2:
                d1.append(pattern[i])
                d2.append(str_list[i])
            elif pattern[i] in d1:
                if d2[d1.index(pattern[i])] != str_list[i]:
                    return False
            elif str_list[i] in d2:
                if d1[d2.index(str_list[i])] != pattern[i]:
                    return False
        return True

    #36 ms
    #时间复杂度O(len(str_list))
    #空间复杂度O(len(pattern)+len(s))
    def wordPattern2(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = s.split(" ")
        n = len(pattern)
        i = 0
        dd_p = {}
        dd_s = {}
        for word in str_list:
            if i == n or dd_p.get(pattern[i], 0) != dd_s.get(word, 0):
                return False
            dd_p[pattern[i]] = dd_s[word] = i + 1
            i += 1
        return i == n


if __name__ == "__main__":
    pattern = "abba"
    # str = "dog dog dog dog"
    str = "dog cat cat dog"
    so = Solution()
    re = so.wordPattern2(pattern, str)
    pass

