# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def creat_tree(self, arr):
        return self._create_tree(arr, None, 0)

    def _create_tree(self, arr, root, i):
        if i >= len(arr):
            return None
        if arr[i] == None:
            arr.insert(2 * i + 1, None)
            arr.insert(2 * i + 2, None)
            return None
        root = TreeNode(arr[i])
        root.left = self._create_tree(arr, root.left, 2 * i + 1)
        root.right = self._create_tree(arr, root.right, 2 * i + 2)
        return root

    def isValidBST(self, root):
        if root == None:
            return True
        compare_val = root.val
        if self.left_tree(root.left, compare_val) and self.right_tree(root.right, compare_val):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False


    def left_tree(self, root, compare_val):
        if root == None:
            return True
        if root.val >= compare_val:
            return False
        return self.left_tree(root.left, compare_val) and self.left_tree(root.right, compare_val)

    def right_tree(self, root, compare_val):
        if root == None:
            return True
        if root.val <= compare_val:
            return False
        return self.right_tree(root.left, compare_val) and self.right_tree(root.right, compare_val)

class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True # ?
        if root.left == root.right == None:
            return True # ?
        if root.left != None and not self.is_left(root.left, root.val):
            return False
        if root.right != None and not self.is_right(root.right, root.val):
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)


    def is_left(self, root, p):
        if root == None:
            return True
        if root.val > p:
            return False
        return self.is_left(root.left, p) and self.is_left(root.right, p)

    def is_right(self, root, p):
        if root == None:
            return True
        if root.val < p:
            return False
        return self.is_right(root.left, p) and self.is_right(root.right, p)















if __name__ == "__main__":
    so = Solution()
    arr = [5, 1, 8, 0, 6, 4, 9]
    root = so.creat_tree(arr)
    re = so.isValidBST(root)
    print(re)
