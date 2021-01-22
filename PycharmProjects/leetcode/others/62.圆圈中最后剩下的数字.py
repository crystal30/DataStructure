class Solution:
    def lastRemaining(self, n: int, m: int):
        if n == 1:
            return n

        n_list = [_ for _ in range(n)]
        i = 0
        len_n = n
        while len_n > 1:
            index = (i + m - 1) % len_n
            n_list.pop(index)
            len_n -= 1
            i = index
        return n_list[0]


if __name__ == "__main__":
    so = Solution()
    n = 10
    m = 17
    re = so.lastRemaining(n, m)
    print(re)