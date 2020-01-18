from collections import Counter
class Solution:
    def __init__(self):
        self.candidates = None
        self.len_candidates = None
        self.res = []
        self.res_dict = []
    def combinationSum2(self, candidates, target: int):
        self.candidates = candidates
        self.len_candidates = len(candidates)
        self.used = [False] * self.len_candidates
        self.subCombinationSum(0, -1, target, [])
        return self.res

    def subCombinationSum(self, start, index, target, subCom):
        if target == 0:
            dict_com = Counter(subCom)
            if dict_com not in self.res_dict:
                self.res_dict.append(dict_com)
                self.res.append(subCom)
            return

        for i in range(start, self.len_candidates):
            e = self.candidates[i]
            if e <= target and i > index:
                subCom.append(e)
                self.subCombinationSum(start, i, target - e, subCom.copy())
                subCom.pop()

            if len(subCom) == 0:
                start += 1

        return

if __name__ == "__main__":
    candidates = [1]
    target = 1
    so = Solution()
    re = so.combinationSum2(candidates, target)
    print(re)
