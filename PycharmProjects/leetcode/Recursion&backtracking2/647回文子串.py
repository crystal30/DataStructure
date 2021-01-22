class Solution:
    def __init__(self):
        self.memo = None
    def countSubstrings(self, s: str):
        len_s = len(s)
        # ? len_s == 0，该怎言处理？
        if len_s == 0:
            return 0
        if len_s == 1:
            return 1
        # memo[i][i] 表示s[i, j]前闭后闭，是否为回文串
        memo = [[0 for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s):
            memo[i][i] = 1

        for i in range(len_s-1, -1, -1):
            for j in range(i+1, len_s):
                # 根据i，j的取值，j-i >= 1
                if j - i <= 2 and s[i] == s[j]:
                    memo[i][j] = 1

                elif j - i > 2 and s[i] == s[j] and memo[i+1][j-1] == 1:
                    memo[i][j] = 1

        return sum([sum(e) for e in memo])

if __name__ == "__main__":
    so = Solution()
    s = "aaa"
    re = so.countSubstrings(s)
    print(re)


