class Node():
    def __init__(self,val=0):
        self.next = dict()
        self.val = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = Node()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self.__root
        for c in key:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]
        cur.val = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.__seekNode(self.__root, prefix,0)
        if node is None:
            return 0
        else:
            return self.__sum(node)

    def __seekNode(self,node,prefix,index):

        if index == len(prefix):
            return node

        pc = prefix[index]
        if pc not in node.next:
            return None
        return self.__seekNode(node.next[pc], prefix, index+1)

    def __sum(self,node):

        sum = node.val
        if len(node.next) == 0:
            return sum
        for c in node.next:
            sum += self.__sum(node.next[c])
        return sum

# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["aa",3], ["a"], ["ab",2], ["a"]]

if __name__ == '__main__':
    sum = MapSum()
    sum.insert('aa',3)
    print(sum.sum('a'))
    sum.insert('ab', 2)
    print(sum.sum('a'))