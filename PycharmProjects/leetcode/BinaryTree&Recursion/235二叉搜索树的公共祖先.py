# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if p.val > q.val:
            p, q = q, p

        if (root.val >= p.val) and (root.val <= q.val):
            return root

        if (root.val > p.val) and (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)

    # 此种情况不用考虑p,q的大小
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        # p, q均 < 当前节点
        if (root.val > p.val) and (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        # p, q均 > 当前节点
        if (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        # 否则(p或q == root，p q在root的两侧)返回root
        return root.val