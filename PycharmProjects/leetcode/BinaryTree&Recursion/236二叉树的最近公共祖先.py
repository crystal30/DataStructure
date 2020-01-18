# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        p_isin_left = self.isin(root.left, p)
        p_isin_right = not p_isin_left

        q_isin_left = self.isin(root.left, q)
        q_isin_right = not q_isin_left

        if (p_isin_left and q_isin_right) or (p_isin_right and q_isin_left):
            return root

        if p_isin_left and q_isin_left:
            return self.lowestCommonAncestor(root.left, p, q)

        if p_isin_right and q_isin_right:
            return self.lowestCommonAncestor(root.right, p, q)


    def isin(self, Node, e):
        if Node == None:
            return False

        if Node.val == e.val:
            return True

        return self.isin(Node.left, e) or self.isin(Node.right, e)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.left.left = None
    root.left.left.right = None
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    so = Solution()
    re = so.lowestCommonAncestor(root, TreeNode(5), TreeNode(1))
    print(re)