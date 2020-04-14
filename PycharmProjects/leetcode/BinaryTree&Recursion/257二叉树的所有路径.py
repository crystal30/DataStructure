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

###############################
# 用全局变量，似乎更好理解哦
class Solution1:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: TreeNode):
        if  root == None:
            return []
        self.binary_tree_path1(root, [])
        return ["->".join(e) for e in self.res]

    def binary_tree_path(self, root, path):
        if root == None:
            self.res.append(path)
            return path

        path.append(str(root.val))
        if root.left == None and root.right == None:
            self.res.append(path.copy())
            return path

        if root.left == None:
            return self.binary_tree_path(root.right, path.copy())

        if root.right == None:
            return self.binary_tree_path(root.left, path.copy())

        self.binary_tree_path(root.left, path.copy())
        self.binary_tree_path(root.right, path.copy())
        return path

    # 这里return 为空也可以哦，因为我们这里用了全局变量，不需要返回东西。
    def binary_tree_path1(self, root, path):
        if root == None:
            self.res.append(path)
            return

        path.append(str(root.val))
        if root.left == None and root.right == None:
            self.res.append(path.copy())
            return

        if root.left == None:
            self.binary_tree_path(root.right, path.copy())
            return

        if root.right == None:
            self.binary_tree_path(root.left, path.copy())
            return

        self.binary_tree_path1(root.left, path.copy())
        self.binary_tree_path1(root.right, path.copy())
        return

    def create_tree(self, arr):
        return self.__create_tree(arr, None, 0)

    def __create_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        if arr[i] == None:
            arr.insert(2*i+1, None)
            arr.insert(2*i+2, None)
            return None

        root = TreeNode(arr[i])
        root.left = self.__create_tree(arr, root.left, 2*i+1)
        root.right = self.__create_tree(arr, root.right, 2*i+2)
        return root

if __name__ == "__main__":

    so = Solution1()
    arr = [1,2,3,None,5]
    # root = so.create_tree(arr)
    # re = so.binaryTreePaths(root)
    # print(re)

    def multiplier():
        ret = [lambda x: i*x for i in range(4)]
        return ret

    print([m(2) for m in multiplier()])

    print(list(filter(lambda n: n%2 == 1, range(1, 10))))


