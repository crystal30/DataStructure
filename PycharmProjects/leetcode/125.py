class Solution:
    def isPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return 'true'

        i = 0
        j = n-1
        s = s.lower()
        while i < j:
            if s[i] not in '0123456789qwertyuiopasdfghjklzxcvbnm':
                i += 1
                continue
            if s[j] not in '0123456789qwertyuiopasdfghjklzxcvbnm':
                j -= 1
                continue
            if s[i] != s[j]:
                return 'false'
            else:
                i += 1
                j -= 1

        return 'true'


if __name__ == "__main__":

    s = "race a car"

    so = Solution()
    re = so.isPalindrome(s)
    pass


