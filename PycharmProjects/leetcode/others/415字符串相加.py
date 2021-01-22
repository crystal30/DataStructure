class Solution:
    def addStrings(self, num1: str, num2: str):
        len_num1 = len(num1)
        len_num2 = len(num2)
        i = len_num1 - 1
        j = len_num2 - 1
        rest = 0
        re = []
        while i >= 0 and j >= 0:
            sub_num1 = num1[i]
            sub_num2 = num2[j]
            sub_re = str(int(sub_num1) + int(sub_num2) + rest)
            if len(sub_re) == 2:
                rest = int(sub_re[0])
                re.insert(0, sub_re[1])
            else:
                rest = 0
                re.insert(0, sub_re)

            i -= 1
            j -= 1

        if i < 0 and j >= 0:
            while j >= 0:
                sub_re = str(int(num2[j]) + rest)
                if len(sub_re) == 2:
                    rest = int(sub_re[0])
                    re.insert(0, sub_re[1])
                else:
                    rest = 0
                    re.insert(0, sub_re)
                j -= 1

        if j < 0 and i >= 0:
            while i >= 0:
                sub_re = str(int(num1[i]) + rest)
                if len(sub_re) == 2:
                    rest = int(sub_re[0])
                    re.insert(0, sub_re[1])
                else:
                    rest = 0
                    re.insert(0, sub_re)
                i -= 1

        # 走到这里，肯定是i==0 and j==0
        if rest != 0:
            re.insert(0, str(rest))
        return "".join(re)

if __name__ == "__main__":
    so = Solution()
    num1 = "9"
    num2 =  "99"
    re = so.addStrings(num1, num2)
    print(re)


