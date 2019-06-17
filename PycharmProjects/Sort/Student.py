class Student():
    def __init__(self, name,score):
        self.name = name
        self.score = score

    #重载<方法，按照我们的要求进行排序
    def __lt__(self, other):

        return  True if self.score > other.score else True if self.name < other.name else False

    def __repr__(self):
        return "Student:{}, {}".format(self.name, self.score)


