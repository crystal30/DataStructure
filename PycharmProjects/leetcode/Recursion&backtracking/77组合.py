class Solution:
    def __init__(self):
        self.res_list = []
        self.not_used = None
    def combine(self, n: int, k: int):
        if n == k:
            return [[i+1 for i in range(n)]]
        self.not_used = [i+1 for i in range(n)]
        self.generation_combine(self.not_used.copy(), k, 0, [])
        return self.res_list

    # index == len(sub_combine)
    def generation_combine(self, not_used, k, index, sub_combine):
        if index == k:
            self.res_list.append(sub_combine)
            return

        while len(not_used) >= k - index:
            e = not_used.pop()
            sub_combine.append(e)
            self.generation_combine(not_used.copy(), k, index + 1, sub_combine.copy())
            sub_combine.pop()

        return


if __name__ == "__main__":
    so = Solution()
    re = so.combine(5,3)
    print(re)


