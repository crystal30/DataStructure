
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

class Solution3:
    def create_tree(self, arr):
        return self._crate_tree(arr, None, 0)

    def _crate_tree(self, arr, root, i):
        if i >= len(arr):
            return None
        if arr[i] == None:
            arr.insert(2*i+1, None)
            arr.insert(2*i+2, None)
            return None
        root = TreeNode(arr[i])
        root.left = self._crate_tree(arr, root, 2*i+1)
        root.right = self._crate_tree(arr, root, 2*i+2)
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return root

        if root.val == key:
            # root 只有左子树
            if root.right == None:
                return root.left
            # root 只有右子树
            if root.left == None:
                return root.right

            # root既有左子树，又有右子树
            min_node = self.find_min_node(root.right)  # 先找到右子树最小的节点min_node
            node = self.delete_min_node(root.right) # 删除右子树最小的节点，
            min_node.left = root.left
            min_node.right = node
            return min_node

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def find_min_node(self, node):
        if node == None:
            return None
        if node.left == None:
            return node
        return self.find_min_node(node.left)

    def delete_min_node(self, node):
        if node == None:
            return None
        if node.left == None:
            return node.right
        node.left = self.delete_min_node(node.left)
        return node


if __name__ == "__main__":
    so = Solution3()
    arr = [5,3,6,2,4,None,7]
    root = so.create_tree(arr)
    re = so.deleteNode(root, 5)
    print("ok")
    # re = so.deleteNode(arr, 3)
    pass