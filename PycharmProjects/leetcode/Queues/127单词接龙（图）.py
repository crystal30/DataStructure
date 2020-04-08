from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        q = [[beginWord, 1]]
        visit = dict()
        visit[beginWord] = True
        word_len = len(beginWord)

        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        while q != []:
            current_word, step = q.pop(0)

            for i in range(word_len):
                inter_word = current_word[:i] + "*" + current_word[i + 1:]

                for word in all_combo_dict[inter_word]:
                    if visit.setdefault(word, False) == False:
                        if word == endWord:
                            return step + 1

                        q.append([word, step + 1])
                        visit[word] = True

        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList):
        q = deque()
        q.append([beginWord, 0])

        visited_word = dict()
        visited_word[beginWord] = True

        if endWord not in wordList:
            return 0

        all_combo_dict = defaultdict(list)
        word_len = len(beginWord)

        for word in wordList:
            for i in range(word_len):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        while len(q) != 0:
            current_word, step = q.popleft()
            if current_word == endWord:
                return step + 1

            for i in range(word_len):
                inter_word = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict[inter_word]:
                    if visited_word.setdefault(word, False) == False:
                        q.append([word, step + 1])
                        visited_word[word] = True

        return 0

if __name__ == "__main__":
    so = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    # beginWord = "leet"
    # endWord = "loot"
    # wordList = ["loot", "loet"]

    # beginWord = "a"
    # endWord = "c"
    # # wordList = ["b", "c", "d"]
    # wordList = ["b", "d", "c"]

    # beginWord = "leet"
    # endWord = "code"
    # wordList = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]

    re = so.ladderLength1(beginWord, endWord, wordList)
    print(re)


