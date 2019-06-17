from BST import BST

class Set():
    def __init__(self):
        self.bst = BST()

    def add(self, e):
        self.bst.add(e)

    def contains(self,e):
        return self.bst.contains(e)

    def remove(self, e):
        self.bst.remove(e)

    #返回set中大于等于e的最小元素
    def ceil(self, e):
        pass

    #返回set中小于等于e的最大元素
    def floor(self, e):
        pass

    def getSize(self):
        return self.bst.getSize()

    def isEmpty(self):
        return self.bst.isEmpty()

if __name__ == '__main__':
    set1 = Set()
    words = ['we','we','asd','de','asd']
    for word in words:
        set1.add(word)
    print(set1.getSize())
    print (set1.contains('asd'))
    set1.remove('asd')
    print(set1.contains('asd'))
    print(set1.isEmpty())

