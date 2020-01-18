from collections import defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # List[List[str]]:
        q = [[beginWord, 1]]
        visit = dict()
        visit[beginWord] = True
        len_word = len(beginWord)

        path = [[beginWord]]
        com_word = defaultdict(list)
        for word in wordList:
            for i in range(len_word):
                com_word[word[:i] + "*" + word[i+1 :]].append(word)


        while q != []:
            c_word, step = q.pop(0)
            for i in range(len(path)):
                if len(path[i]) == step:
                    path[i].append(c_word)

                elif len(path[i]) == 1:
                    path.append(path[i][:-1])
                    path[-1].append(c_word)
                    break


            for i in range(len_word):
                inter_word = c_word[:i] + "*" + c_word[i+1 :]

                for word in com_word[inter_word]:
                    if word == endWord:
                        return path
                    if visit.setdefault(word, False) == False:
                        q.append([word, step + 1])
                        visit[word] = True


        return []

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    so = Solution()
    re = so.findLadders(beginWord, endWord, wordList)
    print(re)
