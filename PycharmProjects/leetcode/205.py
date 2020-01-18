class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        n = len(s)

        for i in range(n):
            if s[i] not in s_dict:
                if t[i] not in s_dict.values():
                    s_dict[s[i]] = t[i]
                else:
                    return False

            else:
                if s_dict[s[i]] != t[i]:
                    return False

        return True

if __name__ == "__main__":
    so = Solution()
    s = "paper"
    t = "title"
    re = so.isIsomorphic(s, t)
    print(re)
