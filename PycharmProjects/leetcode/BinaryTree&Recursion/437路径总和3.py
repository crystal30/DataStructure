# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return 0

        re = self.subpathSum(root, sum)

        if root.left != None:
            re += self.pathSum(root.left, sum)

        if root.right != None:
            re += self.pathSum(root.right, sum)

        return re

    def subpathSum(self, Node, sum):
        re = 0
        if Node == None:
            return 0

        if Node.val == sum:
            re += 1

        l_re = self.subpathSum(Node.left, sum - Node.val)
        r_re = self.subpathSum(Node.right, sum - Node.val)

        return l_re + r_re + re

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    so = Solution()
    re = so.pathSum(root, 8)
    pass