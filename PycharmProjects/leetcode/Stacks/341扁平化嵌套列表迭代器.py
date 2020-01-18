# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def build_gengrator(nestedList):
            for i in nestedList:
                if i.isInteger:
                    yield i.getInteger
                else:
                    i = i.getList()
                    for j in build_gengrator(i):
                        yield j

        self.g = build_gengrator(nestedList)

    def next(self) -> int:
        return self.v

    def hasNext(self) -> bool:
        try:
            self.v = next(self.g)
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    so = NestedIterator([[1,1], 2, [1,1]])
    v = []
    while so.hasNext():
        v.append(so.next())
    pass