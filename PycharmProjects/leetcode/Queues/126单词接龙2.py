from collections import defaultdict, deque

##########################
#该版本超出时间限制

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        len_word = len(beginWord)
        if endWord not in wordList:
            return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        len_word_list = len(wordList)

        # 生成有连接点的图
        g = defaultdict(list)
        for i in range(len_word_list):
            for j in range(i+1, len_word_list):
                if self.similar_word(wordList[i], wordList[j], len_word):
                    g[i].append(j)
                    g[j].append(i)


        distance = defaultdict(int)
        begin = wordList.index(beginWord)
        end = wordList.index(endWord)
        self.bfs(begin, end, distance, g)

        path = [begin]
        res = []

        self.get_res(begin, end, g, distance, path, res, wordList)
        return res

    def bfs(self, begin, end, distance, g):
        q = deque()
        q.append([begin, 0])

        distance[begin] = 0
        while len(q) != 0:
            cur, step = q.popleft()
            for simlar_word_index in g[cur]:
                if simlar_word_index not in distance:
                    distance[simlar_word_index] = step + 1
                    q.append([simlar_word_index, step + 1])

                    if simlar_word_index == end:
                        break

    def get_res(self, cur, end, g, distance, path, res, wordList):
        if len(path) > 0 and path[-1] == end:
            res.append(self.get_path(path, wordList))
            return

        for i in g[cur]:
            if distance[i] == distance[cur] + 1:
                path.append(i)
                self.get_res(i, end, g, distance, path, res, wordList)
                path.pop()
        return

    def get_path(self, path, wordList):
        res = []
        for d in path:
            res.append(wordList[d])

        return res

    def similar_word(self, word1, word2, len_word):
        # 注：传进来的word1，word2 肯定是不同的
        diff_count = 0
        for i in range(len_word):
            if word1[i] != word2[i]:
                diff_count += 1

        if diff_count == 1:
            return True
        else:
            return False

###########################
# 该版本依旧超出时间限制
class Solution1:
    def findLadders(self, beginWord, endWord, wordList):
        len_word = len(beginWord)
        if endWord not in wordList:
            return []

        if beginWord not in wordList:
            wordList.append(beginWord)

        len_word_list = len(wordList)

        # 生成有连接点的图，这一点是否可以改进一下？
        g = defaultdict(list)
        for i in range(len_word_list):
            for j in range(i+1, len_word_list):
                if self.similar_word(wordList[i], wordList[j], len_word):
                    g[i].append(j)
                    g[j].append(i)


        distance = defaultdict(int)
        begin = wordList.index(beginWord)
        end = wordList.index(endWord)
        self.bfs(begin, end, distance, g)

        path = [begin]
        res = []

        self.get_res(begin, end, g, distance, path, res, wordList)
        return res

    def bfs(self, begin, end, distance, g):
        q = deque()
        q.append([begin, 0])

        distance[begin] = 0
        while len(q) != 0:
            cur, step = q.popleft()
            for simlar_word_index in g[cur]:
                if simlar_word_index not in distance:
                    distance[simlar_word_index] = step + 1
                    q.append([simlar_word_index, step + 1])

                    if simlar_word_index == end:
                        break

            if end in distance:
                break

    def get_res(self, cur, end, g, distance, path, res, wordList):
        if len(path) > 0 and path[-1] == end:
            res.append(self.get_path(path, wordList))
            return

        for i in g[cur]:
            if distance[i] == distance[cur] + 1:
                path.append(i)
                self.get_res(i, end, g, distance, path, res, wordList)
                path.pop()
        return

    def get_path(self, path, wordList):
        res = []
        for d in path:
            res.append(wordList[d])

        return res

    def similar_word(self, word1, word2, len_word):
        # 注：传进来的word1，word2 肯定是不同的
        diff_count = 0
        for i in range(len_word):
            if word1[i] != word2[i]:
                diff_count += 1

        if diff_count == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    so = Solution()
    re = so.findLadders(beginWord, endWord, wordList)
    print(re)
