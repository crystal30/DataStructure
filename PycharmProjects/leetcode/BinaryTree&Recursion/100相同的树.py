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

###################
# 这一版代码和上一版代码的思路一样，但是加入了调试的信息，方便理解递归的过程
class Solution1:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False

        if p.val != q.val:
            return False

        # 此递归的过程是左右一起的，类似于 226翻转二叉树中的
        # root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        # print("进入循环前：", p.val, q.val)
        res = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # print("出循环后：", p.val, q.val)

        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    so = Solution1()
    re = so.isSameTree(root, root1)
    print(re)
    pass
