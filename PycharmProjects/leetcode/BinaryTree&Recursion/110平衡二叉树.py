# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True

        if abs(self.maxDep(root.left) - self.maxDep(root.right))> 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDep(self, Node):

        if Node == None:
            return 0

        leftMaxDep = self.maxDep(Node.left)
        rightMaxDep = self.maxDep(Node.right)

        return max(leftMaxDep, rightMaxDep) + 1

    def minDep(self, Node):
        if Node == None:
            return 0

        leftMinDep = self.minDep(Node.left)
        rightMinDep = self.minDep(Node.right)

        # if leftMinDep == 0:
        #     return rightMinDep + 1
        #
        # if rightMinDep == 0:
        #     return leftMinDep + 1

        return min(leftMinDep, rightMinDep) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    so = Solution()
    re = so.isBalanced(root)
    print(re)
    pass