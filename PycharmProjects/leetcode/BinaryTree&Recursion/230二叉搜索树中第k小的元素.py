# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ordered_list = self.in_order(root, [])
        return ordered_list[k-1]


    def in_order(self, root, ordered_list):
        if root == None:
            return ordered_list

        self.in_order(root.left, ordered_list)
        ordered_list.append(root.val)
        self.in_order(root.right, ordered_list)

        return ordered_list

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    so = Solution()
    re = so.kthSmallest(root, 4)
    print(re)


