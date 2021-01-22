class UnionFind:
    def __init__(self, size, accounts):
        self.parent = [i for i in range(size)]
        self.accounts = [None for _ in range(size)]
        for i in range(size):
            self.accounts[i] = list(set(accounts[i][1:]))

    def find(self, x):
        if x != self.parent[x]:
            ori_counts = set(self.accounts[self.parent[x]])
            self.parent[x] = self.find(self.parent[x])
            self.accounts[x] = list(set(self.accounts[x]) | ori_counts)
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        self.parent[root_y] = root_x
        self.accounts[root_x] = list(set(self.accounts[root_x]) | set(self.accounts[root_y]))
        return

    def get_union(self, x):
        root_x = self.find(x)
        if root_x != x:
            return []
        else:
            return self.accounts[x]

class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        if n == 0:
            return accounts
        union_find = UnionFind(n, accounts)
        map_value = dict()
        for i, sub_counts in enumerate(accounts):
            len_sub_counts = len(sub_counts)
            for j in range(1, len_sub_counts):
                if sub_counts[j] in map_value:
                    id = map_value[sub_counts[j]]
                    union_find.union(id, i)

                else:
                    map_value[sub_counts[j]] = i


        re = []
        for i in range(n):
            union_accounts = union_find.get_union(i)
            if len(union_accounts) != 0:
                sub_re = [accounts[i][0]]
                union_accounts.sort()
                sub_re.extend(union_accounts)
                re.append(sub_re)
        return re


if __name__ == '__main__':
    accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
                ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
                ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
                ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
                ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
    so = Solution()
    re = so.accountsMerge(accounts)
    print(re)







