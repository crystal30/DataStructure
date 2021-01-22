class Solution:
    def myAtoi(self, s: str):
        valid_word = "+-0123456789"
        s = s.strip()
        len_s = len(s)
        if len_s == 0:
            return 0
        if s[0] not in valid_word:
            return 0
        end_i = 0
        for i in range(1, len_s):
            if s[i] not in "0123456789":
                break
            end_i = i
        if end_i == 0:
            if s[0] in "+-":
                return 0
            else:
                return int(s[0])
        int_s = int(s[:end_i+1])

        if int_s < -2147483648:
            return -2147483648
        elif int_s > 2147483647:
            return 2147483647
        else:
            return int_s

if __name__ == "__main__":
    so = Solution()
    s = "-+"
    re = so.myAtoi(s)
    print(re)

