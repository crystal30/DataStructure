class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode):
        if root == None:
            return 0

        dep = 1
        return self.depth(root, dep)

    def depth(self, node, dep):
        if node == None:
            return 10000000000  # node == None,将该分支舍去，肯定取不到该分支的深度。
                                # 故将其返回一个很大的值，最终取不为None的那一个分支

        if node.left == None and node.right == None:
            return dep

        # node.left != None and node.right != None
        dep += 1
        dep = min(self.depth(node.left, dep), self.depth(node.right, dep))
        return dep

######################
# 第2个solution的解法更清晰哦
class Solution2:

    def minDepth(self, root: TreeNode):
        return self.min_depth(root, 0)

    def min_depth(self, root: TreeNode, min_deep):
        if root == None:
            return min_deep

        # 只有左子树的情况
        if root.left != None and root.right == None:
            min_deep = self.min_depth(root.left, min_deep + 1)

        # 只有右子树的情况
        elif root.right != None and root.left == None:
            min_deep = self.min_depth(root.right, min_deep + 1)

        # 既有左子树，又有右子树
        else:
            min_deep = min(self.min_depth(root.left, min_deep + 1), self.min_depth(root.right, min_deep + 1))

        return min_deep


##############
class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        if root.right == None:
            return self.minDepth(root.left) + 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1










































