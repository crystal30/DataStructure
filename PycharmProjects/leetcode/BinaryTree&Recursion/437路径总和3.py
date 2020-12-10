# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return 0

        re = self.subpathSum(root, sum)

        if root.left != None:
            re += self.pathSum(root.left, sum)

        if root.right != None:
            re += self.pathSum(root.right, sum)

        return re

    def subpathSum(self, Node, sum):
        re = 0
        if Node == None:
            return 0

        if Node.val == sum:
            re += 1

        l_re = self.subpathSum(Node.left, sum - Node.val)
        r_re = self.subpathSum(Node.right, sum - Node.val)

        return l_re + r_re + re

from copy import copy
class Solution1:
    def create_tree(self, arr):
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


    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return 0

        print("进循环：", root.val)
        rel = self.pathSum(root.left, sum)
        rer = self.pathSum(root.right, sum)
        re = self._path_sum(root, sum)
        print("出循环：", root.val, re + rel + rer)
        return re + rel + rer

    def _path_sum(self, root, sum):
        re = 0
        if root == None:
            return 0

        print("进：", root.val, sum)
        sum -= root.val
        if sum == 0:
            re += 1

        lre = self._path_sum(root.left, sum)
        rre = self._path_sum(root.right, sum)
        print("出：", root.val, sum, re)
        return re + lre + rre

# 思路，先求出所有的路径，然后再找到路径个树

class Solution3:
    def __init__(self):
        self.path_num = 0
        self.path_list = []

    def create_tree(self, arr):
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

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return self.path_num
        self._path_sum(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.path_num

    def _path_sum(self, root, sum_re):
        if root == None:
            return
        sum_re = sum_re - root.val
        if sum_re == 0:
            self.path_num += 1

        self._path_sum(root.left, sum_re)
        self._path_sum(root.right, sum_re)
        return


if __name__ == "__main__":
    arr = [10,5,-3,3,2,None,11,3,-2,None,1]
    # arr1 = [5, 3, 2, 3, -2, None, 1]
    # arr2 = [3, -2, 2]
    # arr3 = [2, None, 8]
    # arr4 = [-3, None, 11]

    so = Solution3()
    root = so.create_tree(arr)
    re = so.pathSum(root, 8)
    print(re)