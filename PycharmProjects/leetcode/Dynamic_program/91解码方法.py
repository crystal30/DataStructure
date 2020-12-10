class Solution:
    def __init__(self):
        self.memo = dict()
    def numDecodings(self, s: str):
        return self._num_decode(s)

    def _num_decode(self, s):
        if self.memo.get(s, -1) != -1:
            return self.memo[s]

        len_s = len(s)
        if len_s >= 2 and s[0] == '0':
            return 0
        if len_s <= 1:
            if s != '0':
                return 1
            else:
                return 0

        res = 0
        for i in range(1, len_s+1):
            if 0< int(s[:i]) <= 26:
                res += self._num_decode(s[i :])

        self.memo[s] = res
        return res



class Solution2:
    def __init__(self):
        self.dict_memo = dict()
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        if s[0] == '0' or (s[1] == '0' and int(s) > 26):
            return 0
        return self._num_decoding(s)

    def _num_decoding(self, s):
        if self.dict_memo.get(s, -1) == -1:
            int_s = int(s)
            # 注意s中含有0的情况
            if len(s) == 2:
                if s[0] == '0' or (s[1] == '0' and int_s > 26):
                    return -1
                elif int_s <= 26:
                    return 2
                else:
                    return 1
            if len(s) == 1:
                if int(s) != 0:
                    return 1
                else:
                    return 0

            two_int_s = int(s[:2])
            if s[0] == '0' or (s[1] == '0' and two_int_s > 26):
                return -1
            if two_int_s > 26:
                self.dict_memo[s] = self._num_decoding(s[1:])
            elif two_int_s == 20 or two_int_s == 10:
                self.dict_memo[s] = self._num_decoding(s[2:])
            else:
                self.dict_memo[s] = self._num_decoding(s[1:]) + self._num_decoding(s[2:])

        return self.dict_memo[s]


if __name__ == "__main__":
    so = Solution2()
    re = so.numDecodings('12')
    print(re)























