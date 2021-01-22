# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        if root.left == None and root.right == None:
            return

        if root.left == None:
            self.flatten(root.right)
            return
        if root.right == None:
            root.right = root.left
            self.flatten(root.left)
            root.left = None
            return

        root_right = root.right
        root.right = root.left
        self.flatten(root.left)
        root.left = None
        while(root.right != None):
            root = root.right
        root.right = root_right
        self.flatten(root_right)
        return

if __name__ == '__main__':
    so = Solution()
    array = [1,2,5,3,4,None,6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    so.flatten(root)
