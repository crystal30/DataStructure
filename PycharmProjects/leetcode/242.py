from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = Counter(s)
        t_dict = Counter(t)

        if s_dict == t_dict:
            return True
        else:
            return False

    def isAnagram1(self, s: str, t: str) -> bool:

        s_dict = dict()
        t_dict = dict()

        for e in s:
            if e not in s_dict:
                s_dict[e] = 1
            else:
                s_dict[e] += 1

        for e in t:
            if e not in t_dict:
                t_dict[e] = 1
            else:
                t_dict[e] += 1

        if s_dict == t_dict:
            return True
        else:
            return False

if __name__ == "__main__":
    so = Solution()
    s = "rat"
    t = "car"
    re = so.isAnagram1(s, t)
    print(re)




