# Definition for a binary tree node.
# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        re = []
        return self.path(root, re)

    def path(self, Node, re):
        if Node == None:
            return re

        if re == []:
            re.append(str(Node.val))
        else:
            re[-1] = re[-1] + '->' + str(Node.val)

        if Node.left == None and Node.right != None:
            return self.path(Node.right, re)

        if Node.left != None and Node.right == None:
            return self.path(Node.left, re)

        if Node.left == None and Node.right == None:
            return re

        l_re = re.copy()
        r_re = re.copy()
        l_re = self.path(Node.left, l_re)
        r_re = self.path(Node.right, r_re)
        l_re.extend(r_re)

        return l_re

###############################
# 用全局变量，似乎更好理解哦
class Solution1:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: TreeNode):
        if  root == None:
            return []
        self.binary_tree_path1(root, [])
        return ["->".join(e) for e in self.res]

    def binary_tree_path(self, root, path):
        if root == None:
            self.res.append(path)
            return path

        path.append(str(root.val))
        if root.left == None and root.right == None:
            self.res.append(path.copy())
            return path

        if root.left == None:
            return self.binary_tree_path(root.right, path.copy())

        if root.right == None:
            return self.binary_tree_path(root.left, path.copy())

        self.binary_tree_path(root.left, path.copy())
        self.binary_tree_path(root.right, path.copy())
        return path

    # 这里return 为空也可以哦，因为我们这里用了全局变量，不需要返回东西。
    def binary_tree_path1(self, root, path):
        if root == None:
            self.res.append(path)
            return

        path.append(str(root.val))
        if root.left == None and root.right == None:
            self.res.append(path.copy())
            return

        if root.left == None:
            self.binary_tree_path(root.right, path.copy())
            return

        if root.right == None:
            self.binary_tree_path(root.left, path.copy())
            return

        self.binary_tree_path1(root.left, path.copy())
        self.binary_tree_path1(root.right, path.copy())
        return

    def create_tree(self, arr):
        return self.__create_tree(arr, None, 0)

    def __create_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        if arr[i] == None:
            arr.insert(2*i+1, None)
            arr.insert(2*i+2, None)
            return None

        root = TreeNode(arr[i])
        root.left = self.__create_tree(arr, root.left, 2*i+1)
        root.right = self.__create_tree(arr, root.right, 2*i+2)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import copy
class Solution3:
    def create_tree(self, arr):
        return self._create_tree(arr, None, 0)

    def _create_tree(self, arr, root, i):
        if i >= len(arr):
            return None
        if arr[i] == None:
            arr.insert(2*i+1, None)
            arr.insert(2*i+2, None)
            return None

        root = TreeNode(arr[i])
        root.left = self._create_tree(arr, root.left, 2*i+1)
        root.right = self._create_tree(arr, root.right, 2*i+2)
        return root

    def __init__(self):
        self.re = []
    def binaryTreePaths(self, root: TreeNode):
        self._binary_tree_path(root, [])
        return ["->".join(e) for e in self.re]

    def _binary_tree_path(self, root, sub_re):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.re.append(sub_re)

        sub_re.append(str(root.val))
        self._binary_tree_path(root.left, copy(sub_re))
        self._binary_tree_path(root.right, copy(sub_re))
        return


if __name__ == "__main__":

    so = Solution3()
    arr = [1,2,3,None,5]
    root = so.create_tree(arr)
    re = so.binaryTreePaths(root)
    print(re)
    # aa = ["1","2","3"]
    # print("->".join(aa))



