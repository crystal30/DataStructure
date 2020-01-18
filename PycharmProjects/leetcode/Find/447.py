class Solution:
    def numberOfBoomerangs(self, points) -> int:
        '''

        :param points: : List[List[int]]
        :return:
        '''

        n = len(points)
        re = 0
        for i in range(n):
            dictij = dict()
            for j in range(n):
                if i != j:
                    dij = self.distance(points[i], points[j])

                    if dij not in dictij:
                        dictij[dij] = 1
                    else:
                        dictij[dij] += 1

            for k in dictij:
                if dictij[k] >= 2:
                    re += dictij[k] * (dictij[k] - 1)


        return re

    # 注意：为防止出现浮点数，故选择距离的平方来代替距离
    def distance(self, point_a, point_b):
        return (point_b[1] - point_a[1]) ** 2 + (point_b[0] - point_a[0]) ** 2

if __name__ == "__main__":
    so = Solution()
    # points = [[0,0],[1,0],[2,0],[3,0]]
    points = [[0,0],[1,0],[0,2]]
    re = so.numberOfBoomerangs(points)
    print(re)