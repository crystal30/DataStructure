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

