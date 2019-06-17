# "A man, a plan, a canal: Panama"
class Solution(object):
    #时间复杂度O(n),空间复杂度O（1）
    #68ms
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
    #初始化一对对撞指针
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isdigit() and not s[i].isalpha():
                i += 1
            elif not s[j].isdigit() and not s[j].isalpha():
                j -= 1
            elif s[i].isdigit() and s[j].isdigit() and s[i]==s[j]:
                i += 1
                j -= 1
            elif s[i].isalpha() and s[j].isalpha() and s[i].upper() == s[j].upper():
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = ".,"
    so = Solution()
    re = so.isPalindrome(s)
    pass