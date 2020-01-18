# Definition for a binary tree node.

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

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    so = Solution()
    re = so.binaryTreePaths(root)
    pass


