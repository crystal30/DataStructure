class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        re = []
        return self.pathS(root, sum, re)

    def pathS(self, Node, sum, re):
        if Node == None:
            return []

        if re == []:
            re.append([Node.val])
        else:
            re[-1].append(Node.val)

        if Node.left == Node.right == None:
            if Node.val == sum:
                return re
            else:
                return []

        re_l = [e.copy() for e in re]
        re_r = [e.copy() for e in re]
        re_l = self.pathS(Node.left, sum - Node.val, re_l)
        re_r = self.pathS(Node.right, sum - Node.val, re_r)
        re_l.extend(re_r)

        return re_l

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    so = Solution()
    re = so.pathSum(root, 22)
    pass



