class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        s_dict= dict()
        pattern_n = len(pattern)
        s_list = str.split(' ')
        s_list_n = len(s_list)

        if pattern_n != s_list_n:
            return False

        for i in range(pattern_n):
            if pattern[i] not in s_dict:
                if s_list[i] not in s_dict.values():
                    s_dict[pattern[i]] = s_list[i]
                else:
                    return False
            else:
                if s_dict[pattern[i]] != s_list[i]:
                    return False
        return True


if __name__ == "__main__":
    so = Solution()
    pattern = "abba"
    str = "dog dog dog dog"
    re = so.wordPattern(pattern, str)
    print(re)
