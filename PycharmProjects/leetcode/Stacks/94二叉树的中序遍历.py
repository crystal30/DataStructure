# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        re = []
        re = self.inorder(root, re)
        return re

    def inorder(self, node, re):
        if node == None:
            return re

        re = self.inorder(node.left, re)
        re.append(node.val)
        re = self.inorder(node.right, re)
        return re

    # 不用递归的中序遍历
    def inorderTraversal1(self, root: TreeNode):
        re = []
        op = []
        op.append([1, root]) # 1 表示访问，0表示打印

        while op != []:
            sub_op = op.pop()
            if sub_op[0] == 1:
                if sub_op[1] != None:
                    op.append([1, sub_op[1].right])
                    op.append([0, sub_op[1]])
                    op.append([1, sub_op[1].left])
            else: # sub_op[0] == 1
                re.append(sub_op[1].val)
        return re




