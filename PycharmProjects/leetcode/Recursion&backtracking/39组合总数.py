from collections import Counter
class Solution:
    def __init__(self):
        self.res = []
        self.res_dict = []
        self.can_min = None
        self.can_max = None
        self.can_n = None

    def combinationSum(self, candidates, target):
        self.can_min = min(candidates)
        self.can_max = max(candidates)
        self.can_n = len(candidates)

        self.generate_combination(candidates, 0, target, [])

        return self.res


    def generate_combination(self, candiates, start, target, combina):
        if target == 0:
            dict_com = Counter(combina)
            if Counter(combina) not in self.res_dict:
                self.res.append(combina)
                self.res_dict.append(dict_com)
            return

        for i in range(start, self.can_n):
            e = candiates[i]
            if target >= self.can_min and target >= e:
                combina.append(e)
                self.generate_combination(candiates, start, target-e, combina.copy())
                combina.pop()

            if len(combina) == 0:
                start += 1
        return


if __name__ == "__main__":
    so = Solution()
    candidates = [2,3,5]
    target = 8
    re = so.combinationSum(candidates, target)
    print(re)
