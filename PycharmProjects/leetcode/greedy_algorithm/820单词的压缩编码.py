from functools import cmp_to_key

# 贪心算法
class Solution:
    def __cmp(self, word_1, word_2):
        len_word_1 = len(word_1)
        len_word_2 = len(word_2)
        return len_word_1 - len_word_2

    def minimumLengthEncoding(self, words):
        len_words = len(words)
        # 由题目可知，len_words > 0
        if len_words == 1:
            return len(words[0]) + 1

        # 将word按从长到短的排列，长的肯定是在字符串中的。
        words_sort = sorted(words, key=cmp_to_key(self.__cmp), reverse=True)
        re = words_sort[0] + "#"
        for i in range(1, len_words):
            words_i = words_sort[i] + "#"
            if words_i not in re:
                re += words_i

        return len(re)


if __name__ == "__main__":
    so = Solution()
    words = ["time", "bell", "me"]
    re = so.minimumLengthEncoding(words)
    print(re)

