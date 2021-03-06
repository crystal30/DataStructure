class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0

        q = [[n, 0]] # n表示当前数字，0：表示有几步到该n
        visit = (n+1) * [False] # wisit 中表示已经访问过的节点
        visit[n] = True
        while q != []:
            num, step = q.pop(0)

            i = 1
            a = num - i * i
            while a >= 0:
                if a == 0:
                    return step + 1
                if visit[a] != True:
                    q.append([a, step + 1])
                    visit[a] = True
                i += 1
                a = num - i * i

    def numSquares1(self, n: int):
        if n == 0:
            return 0

        q = [[n,0]]
        visited = (n+1) * [False]
        visited[n] = True

        while q != []:
            num, step= q.pop(0)

            i = 1
            inter_num = num - i*i
            while inter_num >= 0:
                if inter_num == 0:
                    return step+1

                if visited[inter_num] == False:
                    q.append([inter_num, step + 1])
                    visited[inter_num] = True

                i = i + 1
                inter_num = num - i*i

if __name__ == "__main__":
    n = 12
    so = Solution()
    re = so.numSquares1(n)
    print(re)

