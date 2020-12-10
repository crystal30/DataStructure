# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.left == None:
            return 0 + self.sumOfLeftLeaves(root.right)

        if (root.left.left == None) and (root.left.right == None):
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

###################################
class Solution1:
    def __init__(self):
        self.arr = None

    def create_tree(self, arr):
        self.arr = arr
        return self.__create_tree(None, 0)

    def __create_tree(self,root, i):
        if i >= len(self.arr):
            return None
        if self.arr[i] == None:
            self.arr.insert(2 * i + 1, None)
            self.arr.insert(2 * i + 1, None)
            return None

        root = TreeNode(self.arr[i])
        # print("进入循环前", i, root.val)
        root.left = self.__create_tree(root.left, 2*i+1)
        root.right = self.__create_tree(root.right, 2*i+2)
        # print("出循环", i, root.val)
        return root

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0

        ## 将solution1中的两个if语句合成一个语句啦:)
        if root.left != None and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class Solution3:
    def __init__(self):
        self.re = []
    def create_tree(self, arr):
        self.arr = arr
        return self.__create_tree(None, 0)

    def __create_tree(self,root, i):
        if i >= len(self.arr):
            return None
        if self.arr[i] == None:
            self.arr.insert(2 * i + 1, None)
            self.arr.insert(2 * i + 1, None)
            return None

        root = TreeNode(self.arr[i])
        # print("进入循环前", i, root.val)
        root.left = self.__create_tree(root.left, 2*i+1)
        root.right = self.__create_tree(root.right, 2*i+2)
        # print("出循环", i, root.val)
        return root

    def sumOfLeftLeaves(self, root: TreeNode):
        self._sum_left_leaves(root)
        return sum(self.re)

    def _sum_left_leaves(self, root):
        if root == None:
            return
        if root.left != None and root.left.left == None and root.left.right == None:
            self.re.append(root.left.val)

        self._sum_left_leaves(root.left)
        self._sum_left_leaves(root.right)
        return


if __name__ == "__main__":
    # arr = [5,4,7,3,None,2,None,-1,None,9]
    # arr = [3]
    # arr = []
    arr = [3,9,20,None,None,15,7]
    so = Solution3()
    root = so.create_tree(arr)
    re = so.sumOfLeftLeaves(root)
    print(re)
