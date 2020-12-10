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

        leftmaxDepth = self.maxDepth1(root.left)
        rightmaxDepth = self.maxDepth1(root.right)

        return max(leftmaxDepth, rightmaxDepth) + 1

################

    def maxDepth2(self, root: TreeNode):
        if root == None:
            return 0

        deep = max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1
        return deep

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1







































