# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def create_tree(self, arr):
        return self.__create_tree(arr, 0, None)

    def __create_tree(self, arr, i, root):
        if i >= len(arr):
            return None

        root = TreeNode(arr[i])
        root.left = self.__create_tree(arr, 2*i+1, root.left)
        root.right = self.__create_tree(arr, 2*i+2, root.right)
        return root

    def countNodes(self, root) -> int:
        if root == None:
            return 0

        print("进循环前", root.val)
        res = self.countNodes(root.left) + self.countNodes(root.right) + 1
        print("出循环", root.val, res)
        return res
#######################
#这个题目需要再思考一下，为什么是这样做的呢

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,4,5,6]
    root = so.create_tree(arr)
    re = so.countNodes(root)
    print(re)




