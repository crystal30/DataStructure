# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        sum = sum - root.val
        if root.left == root.right == None:
            return sum == 0

        if root.left == None:
            return self.hasPathSum(root.right, sum)

        if root.right == None:
            return self.hasPathSum(root.left, sum)


        return (self.hasPathSum(root.left, sum)) or (self.hasPathSum(root.right, sum))

    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        sum = sum - root.val
        if root.left == root.right == None:
            return sum == 0

        return (self.hasPathSum(root.left, sum)) or (self.hasPathSum(root.right, sum))

#######################################
class Solution1:
    def create_tree(self, arr):
        return self.__create_tree(arr, None, 0)

    def __create_tree(self, arr, root, i):
        if i >= len(arr) or arr[i] == None:
            return None

        root = TreeNode(arr[i])
        root.left = self.__create_tree(arr, root.left, 2*i+1)
        root.right = self.__create_tree(arr, root.right, 2*i+2)
        return root

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        ## 注意考虑这种边界的情况，和 self.__hasPathSum 中最开始的if结果相冲突
        ## 这种边界情况在具体的题目中需要测一下
        if root == None:
            return False
        return self.__hasPathSum(root, sum)

    def __hasPathSum(self, root, sum):
        if root == None:
            if sum == 0:
                return True
            else:
                return False

        sum = sum - root.val

        ## 注意：需要考虑下边两种if的情况
        if root.left == None:
            return self.__hasPathSum(root.right, sum)

        if root.right == None:
            return self.__hasPathSum(root.left, sum)

        return self.__hasPathSum(root.left, sum) or self.__hasPathSum(root.right, sum)

######################################
## 该道题目没有一次做对哦

class Solution4:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            if root.val == sum:
                return True
            else:
                return False

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)



























if __name__ == "__main__":
    so = Solution1()
    # arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    arr = [5, 8, 4, 13, 4, 11, None, None, None, None, None, 7, 2]
    sum = 22
    root = so.create_tree(arr)
    re = so.hasPathSum(root, sum)
    print(re)



