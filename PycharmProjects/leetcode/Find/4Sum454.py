class Solution:
    #思考：
    #方法一：暴力破解：循环遍历A，B，C，D，时间复杂度O(n4)
    #方法二：将D中的元素放入查找表中（set或map), 再循环遍历A，B, C,时间复杂度O(n3)
    #方法三：将C+D的每一种组合放入查找表中，再循环遍历A，B，时间复杂度O(n2)
    #       这里的查找表到底是用set还是用map？由于C+D可能有重复的值，eg：C=[1,3] D = [2,0]
    #       1+2 == 3+0 == 3,但是这是两种不同的情况，都需要纳入计算，故需用map
    # all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
    # O(n2)的时间复杂度大约为500^2 = 250000，是可以接受的；
    # 而O(n3)时间复杂度大概为500^3=75000000,上亿级别的啦，计算机运行起来会很慢

    #方法三：时间复杂度：O(n2),空间复杂度：O（n2）
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        #由于已知，all A, B, C, D have same length，但即使不符合这个条件，下边的程序也不会报错
        #所以可以添加一个断言
        assert len(A) == len(B) == len(C) == len(D), "A，B，C，D does not meet the requirements"

        dd = {}
        for c in C:
            for d in D:
                dd[c+d] = dd.get(c+d,0)+1
        count = 0
        for a in A:
            for b in B:
                complent = 0 - a - b
                if complent in dd:
                    count += dd[complent]
        return count

    #另一种思路：将A，B放入到一个查找表中，将C，D放入到一个查找表中，
    #时间复杂度O(n2),空间复杂度O(n2)
    #虽然时间复杂度和空间复杂度同fourSumCount，但是由于前边的系数不同，显然fourSumCount1操作更复杂
    #time limit exceeded

    def fourSumCount1(self, A, B, C, D):
        assert len(A) == len(B) == len(C) == len(D), "A, B, C, D does not meet the requirement"
        ddAB = {}
        #时间复杂度O(n2)
        #空间复杂度O(n2)
        for a in A:
            for b in B:
                ddAB[a+b] = ddAB.get(a+b, 0)+1

        ddCD = {}
        #时间复杂度O(n2)
        #空间复杂度O(n2)
        for c in C:
            for d in D:
                ddCD[c+d] = ddCD.get(c+d, 0) + 1
        #时间复杂度O(n2)
        #空间复杂度O（1）
        count = 0
        for k1 in ddAB:
            for k2 in ddCD:
                if k1+k2 == 0:
                    count += ddAB[k1] * ddCD[k2]
        return count



if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    so = Solution()
    re = so.fourSumCount1(A,B,C,D)
    pass




