# Definition for a point.
from fractions import Fraction
from collections import Counter
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
#time limited out
class Solution:
    def maxPoints(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {('inf', 0):1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]:
                    same += 1
                    continue
                if tx == points[i][0]:
                    slope = 'inf'
                    intercept = 0
                else:
                    slope = Fraction((points[i][1] - ty), (points[i][0] - tx))
                    intercept = ty - slope*tx
                dic[(slope,intercept)] = dic.get((slope,intercept),1)+ 1
            m = max(m, max(dic.values()) + same)
        return m
    #勉强通过
    #时间复杂度：O(n2)
    #空间复杂度：O(n)
    #8654ms
    def maxPoints0(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            benchmark_x = points[i][0]
            benchmark_y = points[i][1]
            dic = {('inf', 0):1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == benchmark_x and ty == benchmark_y:
                    same += 1
                    continue
                if tx == benchmark_x:
                    slope = 'inf'
                else:
                    #由于我们固定一个benchmark，看其它点与benchmark是否在一条直线上，
                    # 所以只需要保证斜率相同即可
                    slope = Fraction((benchmark_y- ty), (benchmark_x - tx))
                dic[slope] = dic.get(slope,1)+ 1
            m = max(m, max(dic.values())+same)
        return m

    def maxPoints00(self, points):
        m = 0
        #对于重复的点比较多的情况下，先对其进行分类会更好
        dict_points = Counter([tuple(_) for _ in points])
        dict_points = list(dict_points.items())
        l = len(dict_points)
        for i in range(l):
            k,v = dict_points[i]
            benchmark_x = k[0]
            benchmark_y = k[1]
            dic = {('inf'):v}
            for j in range(i + 1, l):
                tk, tv = dict_points[j]
                tx, ty = tk[0], tk[1]
                if tx == benchmark_x:
                    slope = 'inf'
                else:
                    #由于我们固定一个benchmark，看其它点与benchmark是否在一条直线上，
                    # 所以只需要保证斜率相同即可
                    slope = Fraction((benchmark_y- ty), (benchmark_x - tx))
                dic[slope] = dic.get(slope,v)+ tv
            m = max(m, max(dic.values()))
        return m

    #由于在leetcode中，points的元素为Point类型，所以需要做稍微变动
    def maxPoints1(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'self': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if tx == points[i].x:
                    slope = 'inf'
                    intercept = 0
                elif ty == points[i].y:
                    slope = 0
                    intercept = 0
                elif tx != points[i].x and ty != points[i].y:
                    slope = Fraction((points[i].y - ty), (points[i].x - tx))
                    intercept = ty - slope * tx

                dic[(slope,intercept)] = dic.get((slope,intercept),1)+ 1
            m = max(m, max(dic.values()) + same)
        return m

    #勉强通过
    # 时间复杂度：O(n2)
    # 空间复杂度：O(n)
    # 1654ms
    def maxPoints01(self, points):
        l = len(points)
        m = 0
        for i in range(l):
            benchmark_x = points[i].x
            benchmark_y = points[i].y
            dic = {'inf': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == benchmark_x and ty == benchmark_y:
                    same += 1
                    continue
                if tx == benchmark_x:
                    slope = 'inf'
                else:
                    # 由于我们固定一个benchmark，看其它点与benchmark是否在一条直线上，
                    # 所以只需要保证斜率相同即可
                    slope = Fraction((benchmark_y - ty), (benchmark_x - tx))
                dic[slope] = dic.get(slope, 1) + 1
            m = max(m, max(dic.values()) + same)
        return m

    #700ms
    #时间复杂度：O(n2)
    #空间复杂度：O(n)
    def maxPoints001(self, points):
        m = 0
        #对于重复的点比较多的情况下，先对其进行分类会更好

        points = [(i.x, i.y) for i in points]
        dict_points = Counter([_ for _ in points])
        dict_points = list(dict_points.items())
        l = len(dict_points)
        for i in range(l):
            k,v = dict_points[i]
            benchmark_x = k[0]
            benchmark_y = k[1]
            dic = {('inf'):v}
            for j in range(i + 1, l):
                tk, tv = dict_points[j]
                tx, ty = tk[0], tk[1]
                if tx == benchmark_x:
                    slope = 'inf'
                else:
                    #由于我们固定一个benchmark，看其它点与benchmark是否在一条直线上，
                    # 所以只需要保证斜率相同即可
                    slope = Fraction((benchmark_y- ty), (benchmark_x - tx))
                dic[slope] = dic.get(slope,v)+ tv
            m = max(m, max(dic.values()))
        return m

if __name__ == "__main__":
    points = [[0,0],[1,1],[0,0]]
    so = Solution()
    m = so.maxPoints00(points)
    pass
