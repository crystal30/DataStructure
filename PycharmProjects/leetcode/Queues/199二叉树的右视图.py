class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode):
        re = []
        if root == None:
            return re

        Queue = [[1, root]]
        while Queue != []:
            level, node = Queue.pop(0)

            if level - 1 == len(re):
                re.append(node.val)
            else:
                re[-1] = node.val

            if node.left != None:
                Queue.append([level + 1, node.left])
            if node.right != None:
                Queue.append([level + 1, node.right])

        return re

# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right =



