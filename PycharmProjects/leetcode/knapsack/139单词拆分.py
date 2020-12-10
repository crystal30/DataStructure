class Solution:
    def __init__(self):
        self.memo = dict()
    def wordBreak(self, s, wordDict) -> bool:
        # s 和 wordDict均为非空
        if len(s) == 0:
            return True

        if s in self.memo.keys():
            return self.memo[s]

        re = []
        for word in wordDict:
            re_s = self.word_isvalid(s, word)
            if len(s) != len(re_s):
                re.append(self.wordBreak(re_s, wordDict))

        for sub_re in re:
            if sub_re is True:
                self.memo[s] = True
                return True

        self.memo[s] = False
        return False

    def word_isvalid(self, s, word):
        len_word = len(word)
        if s[:len_word] == word:
            return s[len_word:]
        elif s[-len_word:] == word:
            return s[:-len_word]
        else:
            return s


if __name__ == "__main__":
    so = Solution()
    # s = "catsandog"
    # wordDict = ["cats", "dog", "san", "and", "cat"]
    s = "catskicatcats"
    wordDict = ["cats", "cat", "dog", "ski"]
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    re = so.wordBreak(s, wordDict)
    print(re)
    # re = so.word_isvalid(s, "cats")
    # print(re)