# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        re = []
        self.pre(root, re)
        return re

    def pre(self, node, re):
        if node == None:
            return re

        re.append(node.val)
        re = self.pre(node.left, re)
        re = self.pre(node.right, re)

        return re

    # 不用递归的方法
    def preorderTraversal1(self, root: TreeNode):
        op = []
        op.append([root, 1]) # 1表示访问，0表示打印
        re = []
        while op != []:
            sub_op = op.pop()
            if sub_op[1] == 1:
                if sub_op.node != None:
                    op.append([sub_op.node.right, 1])
                    op.append([sub_op.node.left, 1])
                    op.append([sub_op.node, 0])

            else: # sub_op[0] == 0
                re.append(sub_op[0].val)

        return re


