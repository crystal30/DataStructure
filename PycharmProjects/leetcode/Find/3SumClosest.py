from collections import Counter

class Solution:
    def fourSumCount(self, A, B, C, D):

        re = 0
        target_dict = dict()

        A_dict = Counter(A)
        B_dict = Counter(B)
        C_dict = Counter(C)
        D_dict = Counter(D)

        for a in A_dict.keys():
            for b in B_dict.keys():
                AB_n = A_dict[a] * B_dict[b]

                if 0-a-b not in target_dict:
                    target_dict[0-a-b] = AB_n
                else:
                    target_dict[0-a-b] += AB_n

        for c in C_dict.keys():
            for d in D_dict.keys():
                CD_n = C_dict[c] * D_dict[d]

                if c+d in target_dict.keys():
                    re += target_dict[c+d] * CD_n

        return re

if __name__ == "__main__":
    so = Solution()
    A = [0, 1, -1]
    B = [-1, 1, 0]
    C = [0, 0, 1]
    D = [-1, 1, 1]
    re = so.fourSumCount(A, B, C, D)
    print(re)


