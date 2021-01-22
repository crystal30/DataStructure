# 暴力破解，只能通过10个例子
class Solution:
    def calcEquation(self, equations, values, queries):

        dividend_list = [e[0] for e in equations]
        divisor_list = [e[1] for e in equations]
        only_divisor = set(divisor_list) - set(dividend_list)

        eq_dict = dict()
        for divisor in only_divisor:
            eq_dict[divisor] = 1

        for i, e in enumerate(equations):
            if e[1] in only_divisor:
                eq_dict[e[0]] = values[i]

        for i, e in enumerate(equations):
            dividend = e[0]
            divisor = e[1]
            if dividend in eq_dict.keys() and divisor in eq_dict.keys():
                continue
            elif dividend in eq_dict.keys():
                eq_dict[divisor] = eq_dict[dividend] / values[i]
            elif divisor in eq_dict.keys():
                eq_dict[dividend] = eq_dict[divisor] * values[i]
            else:
                eq_dict[divisor] = 1
                eq_dict[dividend] = values[i]

        re = [-1.0 for _ in range(len(queries))]
        for i, (dividend, divisor) in enumerate(queries):
            if dividend not in eq_dict.keys() or divisor not in eq_dict.keys():
                continue
            else:
                re[i] = eq_dict[dividend] / eq_dict[divisor]

        return re

class Solution1:
    def calcEquation(self, equations, values, queries):
        diviend_list = [e[0] for e in equations]
        divisor_list = [e[1] for e in equations]
        e = set(diviend_list) | set(divisor_list)
        e_degree = dict.fromkeys(e, 0)
        e_adj = dict()
        e_adj_value = dict()
        e_value = dict.fromkeys(e, 1.0)
        for i, (diviend, divisor) in enumerate(equations):
            e_degree[diviend] += 1
            if divisor not in e_adj:
                e_adj[divisor] = [diviend]
                e_adj_value[divisor] = [values[i]]
            else:
                e_adj[divisor].append(diviend)
                e_adj_value[divisor].append(values[i])

        # 不在一个圈圈里的依然不行
        re = [-1.0 for _ in range(len(queries))]
        for i, (diviend, divisor) in enumerate(queries):
            re1 = self.dfs(diviend, divisor, 1, e_adj, e_adj_value)
            if re1 < 0:
                re2 = self.dfs(divisor, diviend, 1, e_adj, e_adj_value)
                if re2 >= 0:
                    re[i] = re2
            else:
                re[i] = re1
        return re

    def dfs(self, diviend, divisor, re, e_adj, e_adj_value):
        if divisor not in e_adj.keys():
            return -1.0

        for i, di in enumerate(e_adj[divisor]):
            if di == diviend:
                re = re * e_adj_value[divisor][i]
                return re

            re = re * self.dfs(diviend, di, re * e_adj_value[divisor][i], e_adj, e_adj_value)
            if re >= 0:
                return re
        return -1.0


if __name__ == '__main__':
    equations = [["a","b"],["b", "c"], ["d","e"], ["e", "c"]]
    values = [1.0, 2.0, 3.0, 4.0]
    queries = [["b","d"],["b","a"],["d","c"]]
    so = Solution1()
    re = so.calcEquation(equations, values, queries)
    print(re)






