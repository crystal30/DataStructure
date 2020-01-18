class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        re = []
        re = self.poster(root, re)
        return re

    def poster(self, node, re):
        if node == None:
            return re

        re = self.poster(node.left, re)
        re = self.poster(node.right, re)
        re.append(node.val)
        return re

    # 不用递归的中序遍历
    def posterTraversal1(self, root: TreeNode):
        re = []
        op = []
        op.append([1, root]) # 1 表示访问，0表示打印

        while op != []:
            sub_op = op.pop()
            if sub_op[0] == 1:
                if sub_op[1] != None:
                    op.append([0, sub_op[1]])
                    op.append([1, sub_op[1].right])
                    op.append([1, sub_op[1].left])
            else: # sub_op[0] == 1
                re.append(sub_op[1].val)
        return re
