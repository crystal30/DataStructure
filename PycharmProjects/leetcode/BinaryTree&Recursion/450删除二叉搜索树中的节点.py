# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return

        # 会不会出现key不在树中的情况呢？
        if root.val == key:
            if root.left == None:
                return root.right

            if root.right == None:
                return root.left

            if root.right != None and root.left != None:
                right_min_node = self.right_minNode(root.right)
                right_min_node.right = self.del_min_node(root.right)
                right_min_node.left = root.left
                return right_min_node

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        if root.val < key:
            root.right = self.deleteNode(root.right, key)


        return root

    # 返回右子树中最小的节点
    def right_minNode(self, Node):
        if Node.left == None:
            return Node

        return self.right_minNode(Node.left)

    # 删除右子树中的最小节点
    def del_min_node(self, Node):
        if Node.left == None:
            noderight = Node.right
            Node.right = None
            return noderight

        Node.left = self.del_min_node(Node.left)
        return Node

class Solution1:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left == None and root.right == None:
                return None

            if root.left == None:
                return root.right

            if root.right == None:
                return root.left

            Node = self.re_min_node(root.right)
            Node.right = self.del_min_node(root.right)
            Node.left = root.left
            return Node

    # 返回右子树中最小的节点
    # 最先输入的Node不为None
    def re_min_node(self, Node):
        if Node.left == None:
            return Node

        return self.re_min_node(Node.left)

    # 删除右边子树中最小的节点
    # 最初始的node不为空
    def del_min_node(self, Node):
        if Node.left == None:
            return Node.right

        Node.left = self.del_min_node(Node.left)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(7)

    so = Solution1()
    re = so.deleteNode(root, 3)
    pass