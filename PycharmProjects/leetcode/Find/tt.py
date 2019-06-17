class BST:
    class __Node():
        def __init__(self, e=None):
            self.e = e
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.e)

    def __init__(self):
        self.root = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

       # 添加元素2
    def add(self, e):
        self.root = self.__add(self.root, e)

    # 返回新插入节点后，二分搜索树的根
    def __add(self, Node, e):
        if Node is None:
            self.size += 1
            return self.__Node(e)

        if Node.e > e:
            Node.left = self.__add(Node.left, e)
        elif Node.e < e:
            Node.right = self.__add(Node.right, e)

        return Node


    # 找二分搜索树中大于等于e的最小元素
    def ceil(self, e):
        return self.__ceil(self.root, e)

    def __ceil(self, Node, e):

        if Node == None:
            return None
        else:
            if Node.e >= e:
                if Node.left != None and Node.left.e >= e:
                    return self.__ceil(Node.left, e)
                return Node.e
            else:
                return self.__ceil(Node.right, e)

    # 删除任意元素
    def remove(self, e):
        self.root = self.__remove(self.root, e)

    # 删除掉以node为根的二分搜索树中值为e的节点, 递归算法
    # 返回删除节点后新的二分搜索树的根
    def __remove(self, Node, e):
        if Node == None:
            return None
        if Node.e > e:
            Node.left = self.__remove(Node.left, e)
        elif Node.e < e:
            Node.right = self.__remove(Node.right, e)
        else:
            # 要删除的节点左子树为空的情况
            if Node.left == None:
                rightNode = Node.right
                Node.right = None
                self.size -= 1
                return rightNode

            # 要删除的节点右子树为空的情况
            if Node.right == None:
                leftNode = Node.left
                Node.left = None
                self.size -= 1
                return leftNode

            # 要删除的节点 左子树和右子数均不为空
            # 找到该节点右子树中最小的节点，成为该节点的后继 sNode
            # 删除该节点右子树最小的节点（sNode），并让sNode.right指向此右子树，
            # sNOde.left 指向该节点的左子树 至此，sNode 已经占据了要删除的节点的位置
            # 删除Node，令Node.right 和 Node.left 均为 None，size --
            if Node.left != None and Node.right != None:
                sNode = self.__minimum(Node.right)
                sNode.right = self.__remove(Node.right, e)
                sNode.left = Node.left
                Node.right = Node.left = None
                return sNode

    def __minimum(self,Node):

        if Node.left == None:
            return Node
        return self.__minimum(Node.left)

class Solution:
    #time limited out
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        record = BST()
        for i in range(len(nums)):
            a = nums[i] - t  # 如果record 中大于等于a的最小的元素 <= nums[i]+t,return True

            if record.ceil(a) is not None and record.ceil(a) <= nums[i] + t:
                return True
            record.add(nums[i])

            if record.getSize() > k:
                record.remove(nums[i - k])
        return False


