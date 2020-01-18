from fractions import Fraction

class Solution:
    def maxPoints(self, points) -> int:
        '''

        :param points: List[List[int]]
        :return:
        '''
        re = 0
        n = len(points)
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(n):
            plot_ij = dict()
            repeat = 0
            for j in range(n):
                if points[j] == points[i]:
                    repeat += 1
                else:
                    if points[j][0] == points[i][0]:
                        plot = 'y'
                    else:
                        plot = Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0])

                    if plot not in plot_ij:
                        plot_ij[plot] = 1
                    else:
                        plot_ij[plot] += 1


            plot_ij_v = list(plot_ij.values())
            if len(plot_ij_v) == 0:
                temp_re = repeat
            else:
                temp_re = max(plot_ij_v) + repeat

            if temp_re > re:
                re = temp_re

        return re

if __name__ == "__main__":
    so = Solution()
    points = [[0,0],[94911151,94911150],[94911152,94911151]]
    re = so.maxPoints(points)
    print(re)
