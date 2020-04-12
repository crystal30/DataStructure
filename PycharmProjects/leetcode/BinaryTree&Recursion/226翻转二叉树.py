# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode):
        if root == None:
            return root

        ### 这样写两条是不行的，思考原因
        # root.right = self.invertTree(root.left)
        # root.left = self.invertTree(root.right)

        # 调试打印内容
        # if root.left == None:
        #     b_root_left = None
        # else:
        #     b_root_left = root.left.val
        #
        # if root.right == None:
        #     b_root_right = None
        # else:
        #     b_root_right = root.right.val
        #
        # print("进入循环前：", root.val, b_root_left, b_root_right)

        # 但是这样写是可以的
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)

        # 调试打印内容
        # if root.left == None:
        #     af_root_left = None
        # else:
        #     af_root_left = root.left.val
        #
        # if root.right == None:
        #     af_root_right = None
        # else:
        #     af_root_right = root.right.val
        #
        # print("出循环", root.val, af_root_left, af_root_right)

        return root

    def creat_tree(self, arr):
        if len(arr) > 0:
            return self.__create_tree(arr, None, 0)

        else:
            return None

    def __create_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        else:
            if arr[i] == 'null':
                return None
            else:
                # 先根，然后左，右。可根据此来判断递归的路径
                root = TreeNode(arr[i])
                root.left = self.__create_tree(arr, root.left, 2*i +1)
                root.right = self.__create_tree(arr, root.right, 2*i +2)
                return root

if __name__ == "__main__":
    so = Solution()
    arr = [4,2,7,1,3,6,9]
    root = so.creat_tree(arr)
    so.invertTree(root)
    pass


