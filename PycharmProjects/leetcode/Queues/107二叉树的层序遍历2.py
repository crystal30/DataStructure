from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root  == None:
            return []

        q = deque()
        q.append([root, 0])
        res = []
        while len(q) != 0:
            node, level = q.popleft()

            if len(res) == level:
                res.insert(0, [node.val])
            else:
                res[0].append(node.val)

            if node.left != None:
                q.append([node.left, level+1])
            if node.right != None:
                q.append([node.right, level+1])

        return res

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    so = Solution()
    res = so.levelOrderBottom(root)
    print(res)