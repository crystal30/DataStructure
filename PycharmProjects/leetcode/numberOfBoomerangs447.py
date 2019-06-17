from scipy.special import comb, perm
class Solution:
    #暴力破解
    #时间复杂度：O(n3)
    #时间复杂度太高
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dis_ij = self.dis(points[i], points[j])
                for k in range(n):
                    if i == k or k == j:
                        continue
                    dis_ik = self.dis(points[i], points[k])
                    if dis_ij == dis_ik:
                        count += 1
        return count

    #为简化起见，下边的函数算出的并不是欧式距离，加一个根号sqrt就是欧式距离了
    def dis(self, a, b):
        return (b[1]-a[1])**2 + (b[0]-a[0])**2

    #方法二：固定i，用O(n)的复杂度从剩下的数组中找出所有的j,k
    #time limited out
    #时间复杂度：O（n2）
    #空间复杂度：O（len(dict_dis)）,但是计算距离时有一些重复的操作
    def numberOfBoomerangs1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count = 0
        for i in range(n):
            dict_dis = dict()
            for j in range(n):
                if i == j:
                    continue
                dis_ij = self.dis(points[i], points[j])
                dict_dis[dis_ij] = dict_dis.get(dis_ij, 0) + 1

            for v in dict_dis.values():
                count += perm(v, 2)
        return int(count)

    #改进方法二，不用perm函数
    #虽然可以通过，但是感觉还不是很理想
    def numberOfBoomerangs2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        count = 0
        for i in range(n):
            dict_dis = dict()
            for j in range(n):
                if i != j:
                    dis_ij = self.dis(points[i], points[j])
                    dict_dis[dis_ij] = dict_dis.get(dis_ij, 0) + 1

            for v in dict_dis.values():
                count += v * (v-1)
        return int(count)

    #看别人的方法,思路很奇特
    #时间复杂度：O(n2)
    #空间复杂度：len（cats）约为O(n)
    def numberOfBoomerangs3(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            cnts = {}

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                d = dx * dx + dy * dy

                if d in cnts:
                    ans += cnts[d]
                    cnts[d] += 1
                else:
                    cnts[d] = 1
        return 2 * ans

if __name__ == "__main__":
    points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    so = Solution()
    re = so.numberOfBoomerangs3(points)
    pass
