class Solution:
    #56ms
    #时间复杂度 O(nlogn)
    #空间复杂度 O(n)
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dd_s = {}
        re = ""
        for c in s:
            dd_s[c] = dd_s.get(c,0)+1
        #上述同样可以用Counter（）
        d_list = [_ for _ in dd_s.items()]
        #时间复杂度O(n)
        self.maxHeap(d_list)
        #时间复杂度O(nlogn)
        for _ in range(len(d_list)):
            e = self.extraMax(d_list)
            re += e[0]*e[1]
        return re

    def maxHeap(self,d_list):

        n = len(d_list)
        for i in range((n-2)//2,-1,-1):
            self.__shiftDown(i,d_list)

    def __shiftDown(self,i,d_list):
        n = len(d_list)
        e = d_list[i][1]
        while i*2+1 < n:
            j = i*2+1 #j中存放i中左右孩子最大的那个元素
            if j+1<n and d_list[j][1] < d_list[j+1][1]:
                j += 1
            if d_list[j][1] > e:
                d_list[j], d_list[i] = d_list[i], d_list[j]
                i = j
            else:
                break
    def extraMax(self,d_list):
        if len(d_list) > 1:
            re = d_list[0]
            d_list[0] = d_list.pop()
            self.__shiftDown(0,d_list)
        else:
            re = d_list.pop()
        return re

if __name__ == "__main__":
    s = "ree"

    # "eert"
    so = Solution()
    re = so.frequencySort(s)
    pass