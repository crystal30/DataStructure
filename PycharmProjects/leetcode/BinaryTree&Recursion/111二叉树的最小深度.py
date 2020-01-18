class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode):
        if root == None:
            return 0

        dep = 1
        return self.depth(root, dep)

    def depth(self, node, dep):
        if node == None:
            return 10000000000  # node == None,将该分支舍去，肯定取不到该分支的深度。
                                # 故将其返回一个很大的值，最终取不为None的那一个分支

        if node.left == None and node.right == None:
            return dep

        # node.left != None and node.right != None
        dep += 1
        dep = min(self.depth(node.left, dep), self.depth(node.right, dep))
        return dep

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.left = TreeNode(18)
    root.right.left.right = TreeNode(19)

    so = Solution()
    mindep = so.minDepth(root)
    print(mindep)



