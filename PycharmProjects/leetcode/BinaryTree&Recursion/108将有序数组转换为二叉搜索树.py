# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        len_num = len(nums)
        if len_num == 0:
            return None
        if len_num == 1:
            return TreeNode(nums[0])
        mid = len_num//2
        root = TreeNode(nums[mid])
        root.left, root.right = self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:])
        return root
