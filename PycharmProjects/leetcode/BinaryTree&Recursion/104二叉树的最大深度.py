# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        dep = 1
        dep = self.depth(root, dep)
        return dep

    def depth(self, node, dep):
        if node == None:
            return dep

        if (node.left == None) and (node.right == None):
            return dep

        dep += 1
        dep = max(self.depth(node.left, dep), self.depth(node.right, dep))
        return dep

    # 更高级的写法，但是感觉比较难想
    def maxDepth1(self, root: TreeNode):
        if root == None:
            return 0

        leftmaxDepth = self.maxDepth(root.left)
        rightmaxDepth = self.maxDepth(root.right)

        return max(leftmaxDepth, rightmaxDepth) + 1


