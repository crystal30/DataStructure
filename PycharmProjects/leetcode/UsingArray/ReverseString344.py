class Solution(object):
    #36ms
    #时间复杂度：O(len(s))
    #空间复杂度：O（len（s））
    #注意str本身不能进行s[i], s[j] = s[j], s[i]，因为字符串是不可变对象
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 对撞指针
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)

if __name__ == "__main__":
    s = 'hello'
    so = Solution()
    re = so.reverseString1(s)
    pass

