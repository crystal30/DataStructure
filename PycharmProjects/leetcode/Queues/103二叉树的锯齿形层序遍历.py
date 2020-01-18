class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):

        re = []
        if root == None:
            return re

        Queue = [[1, root]]
        while Queue != []:
            level, node = Queue.pop(0)

            if level-1 == len(re):
                re.append([])

            if level % 2 == 1:
                re[level - 1].append(node.val)
            else:
                re[level - 1].insert(0, node.val)

            if node.left != None:
                Queue.append([level + 1, node.left])

            if node.right != None:
                Queue.append([level + 1, node.right])

        return re




