# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root_value = preorder[0]
        root = TreeNode(root_value)
        root_index = inorder.index(root_value)
        root.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1+root_index :], inorder[root_index+1 :])
        return root


if __name__ == '__main__':
    so = Solution()
    # preorder = [3,9,20,15,7]
    # inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 16, 15, 20, 15 ,17, 9, 10]
    inorder = [16, 9, 15, 3, 15, 20, 9, 17, 10]
    re = so.buildTree(preorder, inorder)
    print("ok")




