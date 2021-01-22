from copy import copy
class Solution:
    def __init__(self):
        self.re = set()
    def permutation(self, s: str):
        self._permutation(list(s), "")
        return list(self.re)

    def _permutation(self, s_list, sub_s):
        if len(s_list) == 0:
            self.re.add(sub_s)

        for i in range(len(s_list)):
            e = s_list[i]
            s_list1 = copy(s_list)
            s_list1.remove(e)
            self._permutation(s_list1, sub_s+e)

if __name__ == "__main__":
    so = Solution()
    s = "abc"
    re = so.permutation(s)
    print(re)




