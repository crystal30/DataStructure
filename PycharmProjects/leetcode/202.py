class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = n
        re = 0
        re_list = []
        while n1 != 1:

            while n1 > 0:
                n1, mod = divmod(n1, 10)
                re += mod * mod

            if re in re_list:
                return False
            else:
                re_list.append(re)
            n1 = re
            re = 0

        return True

if __name__ == "__main__":
    so = Solution()
    n = 2
    re = so.isHappy(n)
    print(re)