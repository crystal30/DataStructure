from collections import Counter,OrderedDict

class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = OrderedDict()
        re_list = []
        for e in s:
            if e not in s_dict:
                s_dict[e] = 1
            else:
                s_dict[e] += 1

        s_dict = sorted(s_dict.items(), key = lambda t:t[1], reverse = True)

        for e in s_dict:
            for _ in range(e[1]):
                re_list.append(e[0])

        return ''.join(re_list)


if __name__ == "__main__":
    so = Solution()
    s = "Aabb"
    re = so.frequencySort(s)
    print(re)


