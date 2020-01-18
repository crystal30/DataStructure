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