# 最后两个用例超时间
# 注意：一旦某节课上过，就不能再上了
# 思路，怎样把已经上过的课扔掉？
class Solution:
    def canFinish(self, numCourses, prerequisites):
        memo = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        for e in prerequisites:
            memo[e[0]][e[1]] = 1

        memo_sum = sum([sum(e) for e in memo])
        if memo_sum == 0:
            return True
        memo_visited = [False for _ in range(numCourses)]
        while memo_sum != 0:
            memo_row_sum = [sum(e) for e in memo]
            new_no_need_pre = [e for e in enumerate(memo_row_sum)
                               if e[1] == 0 and memo_visited[e[0]] is False]
            if len(new_no_need_pre) == 0:
                return False
            for i, row_sum in new_no_need_pre:
                # 如果第i行==0，则将该列的值全部置为0
                memo_visited[i] = True
                for j in range(numCourses):
                    memo[j][i] = 0
            memo_sum = sum([sum(e) for e in memo])
        return True

# 入度表，广度优先遍历
from collections import deque
class Solution1:
    def canFinish(self, numCourses, prerequisites):
        # 得到入读表，和邻接矩阵
        degree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            degree[cur] += 1
            adj[pre].append(cur)
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adj[pre]:
                degree[cur] -= 1
                if degree[cur] == 0:
                    queue.append(cur)

        return not numCourses

# 深度优先遍历,查看是否有环
class Solution2:
    def canFinish(self, numCourses, prerequisites):
        flags = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)

        for pre in range(numCourses):
            if not self.dfs(pre, adj, flags):
                return False
        return True

    def dfs(self, pre, adj, flags):
        if flags[pre] == 1:
            return False
        if flags[pre] == -1:
            return True
        flags[pre] = 1
        for i in adj[pre]:
            if not self.dfs(i, adj, flags):
                return False
        flags[pre] = -1
        return True


if __name__ == '__main__':
    so = Solution2()
    numCourses = 5
    prerequisites = [[3, 0], [0,3],[1, 0], [2, 1], [4, 2], [4, 3]]
    re = so.canFinish(numCourses, prerequisites)
    print(re)


