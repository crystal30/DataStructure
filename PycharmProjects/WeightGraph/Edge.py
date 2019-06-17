class Edge:
    def __init__(self,a,b,weight):
        self.a = a
        self.b = b
        self.weight = weight

    #返回第一个顶点
    def v(self):
        return self.a

    #返回第二个顶点
    def w(self):
        return self.b

    #返回权值
    def wt(self):
        return self.weight

    #给定一个顶点, 返回另一个顶点
    def other(self, x):
        assert x == self.a or x == self.b, "x must be one of the vertices"
        return self.a if x == self.b else self.b

    #输出边的信息
    def SideInfo(self):
        re = self.a +'-->'+ self.b + ':' + self.weight
        print(re)

    #边之间的比较
    #重构小于函数
    def __lt__(self, other):
       return True if self.weight < other.weight else False

    #重构小于等于函数
    def __le__(self, other):
        return True if self.weight <= other.weight else False

    #重构大于函数
    def __gt__(self, other):
        return True if self.weight > other.weight else False

    #重构大于等于函数
    def __ge__(self, other):
        return True if self.weight >= other.weight else False




