# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def creat_tree(self, arr):
        if len(arr) == 0:
            return None

        return self.__create_tree(arr, None, 0)

    def __create_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        root = arr[i]
        root.left = self.__create_tree(arr, root.left, 2*i+1)
        root.right = self.__create_tree(arr, root.right, 2*i+2)
        return root

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        # 先将左子树翻转
        convert_root_left = self.convert_tree(root.left)
        # 查看翻转后的左子树和右子树是否相同
        return self.is_same_tree(convert_root_left, root.right)

    # 翻转树
    def convert_tree(self, root):
        if root == None:
            return root

        root.left, root.right = self.convert_tree(root.right), self.convert_tree(root.left)
        return root

    # 查看两颗树是否相同
    def is_same_tree(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)

