# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True # 需要用测试用例验证一下
        root.left = self.invertTree(root.left)
        return self.sameTree(root.left, root.right)

    def invertTree(self, node):
        if node == None:
            return None

        node.right, node.left = self.invertTree(node.left), self.invertTree(node.right)
        return node

    def sameTree(self, node1, node2):
        if (node1 == None) and (node2 == None):
            return True

        if (node1 == None) or (node2 == None):
            return False

        if node1.val != node2.val:
            return False

        return (self.sameTree(node1.left, node2.left)) and (self.sameTree(node1.right, node2.right))
