# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        sum = sum - root.val
        if root.left == root.right == None:
            return sum == 0

        if root.left == None:
            return self.hasPathSum(root.right, sum)

        if root.right == None:
            return self.hasPathSum(root.left, sum)


        return (self.hasPathSum(root.left, sum)) or (self.hasPathSum(root.right, sum))

    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        sum = sum - root.val
        if root.left == root.right == None:
            return sum == 0

        return (self.hasPathSum(root.left, sum)) or (self.hasPathSum(root.right, sum))
