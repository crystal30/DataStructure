# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p == None and q == None: # p,q都为None的情况
            return True

        if p == None or q == None: # 两种情况：p为None，q不为None；p不为None，q为None
            return False

        if p.val != q.val: # 在p,q都不为None时，比较节点的值
            return False

        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    so = Solution()
    re = so.isSameTree(root, root1)
    print(re)
    pass
