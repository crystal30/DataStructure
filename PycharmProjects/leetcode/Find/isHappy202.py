from collections import Counter
class Solution:
    #time limited exceeded
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while True:
            str_n = str(n)
            lo = [n]
            n = 0
            for i in str_n:
                n += int(i)**2

            if n == 1:
                return True

            if n not in lo:
                lo.append(n)
            else:
                return False

    #68ms
    #时间复杂度：O(n*len(s)), n表示循环的次数
    #空间复杂度：O(n)
    def isHappy1(self, s):
        x = s
        dd = {}
        while x>1:
            x = self.mysqure(x)
            dd[x] = dd.get(x,0) + 1
            if dd[x]>1:
                return False
        return True

    def mysqure(self, s):
        s_squre_sum = 0
        while s > 0:
            s_squre_sum += (s % 10) ** 2
            s //= 10
        return s_squre_sum

    #108ms 处理起来字符串似乎更慢哟
    def isHappy2(self, s):
        x = s
        dd = {}
        while x>1:
            x = self.mysqure2(x)
            dd[x] = dd.get(x,0) + 1
            if dd[x]>1:
                return False
        return True

    def mysqure2(self, s):
        re = 0
        for i in str(s):
            re += int(i)**2
        return re

if __name__ == "__main__":
    n = 19
    so = Solution()
    re = so.isHappy1(n)
    pass
