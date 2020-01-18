class Solution:
    def letterCombinations(self, digits: str):
        len_digits = len(digits)
        if len_digits == 0:
            return []

        self.dd = dict()
        self.dd['2'] = 'abc'
        self.dd['3'] = 'def'
        self.dd['4'] = 'ghi'
        self.dd['5'] = 'jkl'
        self.dd['6'] = 'mno'
        self.dd['7'] = 'pqrs'
        self.dd['8'] = 'tuv'
        self.dd['9'] = 'wxyz'

        self.n = 1
        for d in digits:
            self.n *= len(self.dd[d])

        re = [''] * self.n
        d_list = list(digits)
        return self.func(d_list, re, 1)

    def func(self, d_list, re, i):
        if d_list == []:
            return re

        d = d_list.pop()
        d_e = self.dd[d]
        len_d_e = len(d_e)
        k = 0
        m = i
        for j in range(self.n):
            re[j] = d_e[k] + re[j]
            m -= 1
            if m == 0:
                k += 1
                m = i

            if k == len_d_e:
                k = 0

        re = self.func(d_list, re, len_d_e * i)
        return re


if __name__ == '__main__':
    so = Solution()
    re = so.letterCombinations('7')
    print(re)



