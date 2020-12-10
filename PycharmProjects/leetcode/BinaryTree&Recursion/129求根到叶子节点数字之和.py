# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode):
        re = []
        re = self.sumNum(root, re)
        return re.sum()

    def sumNum(self, Node, re):
        if Node == None:
            return []

        if re == []:
            re.append(Node.val)
        else:
            re[-1] = re[-1] * 10 + Node.val

        if Node.left == Node.right == None:
            return re

        re_l = re.copy()
        re_r = re.copy()
        re_l = self.sumNum(Node.left, re_l)
        re_r = self.sumNum(Node.right, re_r)
        re_l.extend(re_r)
        return re_l


class Solution1:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode):
        self._sum_numbers(root, 0) # root == None
        return self.sum

    def _sum_numbers(self, root, path_sum):
        if root == None:
            self.sum += path_sum
            return

        path_sum = path_sum*10 + root.val
        if root.left == None:
            self._sum_numbers(root.right, path_sum)

        elif root.right == None:
            self._sum_numbers(root.left, path_sum)

        else:
            self._sum_numbers(root.left, path_sum)
            self._sum_numbers(root.right, path_sum)

        return


class Solution2:
    def __init__(self):
        self.all_re = 0
    def sumNumbers(self, root: TreeNode) -> int:
        self._sumNumbers(root, 0)
        return self.all_re

    def _sumNumbers(self, root, re):
        if root == None:
            return 0
        if root.left == root.right == None:
            self.all_re += re + root.val
            return
        re = re*10 + root.val
        self._sumNumbers(root.left, re)
        self._sumNumbers(root.right, re)
        return























