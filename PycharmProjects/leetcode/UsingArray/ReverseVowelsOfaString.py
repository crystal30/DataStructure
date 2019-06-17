class Solution(object):
    #172ms
    #优化？
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a','e','i','o','u']
        #初始化对撞指针
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i].lower() in vowels and s[j].lower() in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].lower() not in vowels and s[j].lower() not in vowels:
                i += 1
                j -= 1
            elif s[i].lower() in vowels and s[j].lower() not in vowels:
                j -= 1
            else:#s[i].lower() in vowels and s[j].lower() not in vowels:
                i += 1
        return ''.join(s)

    # 对reverseVowels的改进，思路是一样的，只不过是写法不同，少了一些重复的判断
    #84 ms
    def reverseVowels1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u']
        #初始化对撞指针
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i].lower() in vowels:
                if s[j].lower() in vowels:
                    s[i], s[j] = s[j], s[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else: #s[i].lower() not in vowels
                if s[j].lower() not in vowels:
                    i += 1
                    j -= 1
                else:
                    i += 1
        return ''.join(s)

if __name__ == "__main__":
    s = 'hello'
    so = Solution()
    re = so.reverseVowels(s)
    pass