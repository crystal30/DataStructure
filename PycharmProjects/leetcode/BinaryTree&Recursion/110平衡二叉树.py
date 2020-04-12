# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True

        if abs(self.maxDep(root.left) - self.maxDep(root.right))> 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDep(self, Node):

        if Node == None:
            return 0

        leftMaxDep = self.maxDep(Node.left)
        rightMaxDep = self.maxDep(Node.right)

        return max(leftMaxDep, rightMaxDep) + 1

    def minDep(self, Node):
        if Node == None:
            return 0

        leftMinDep = self.minDep(Node.left)
        rightMinDep = self.minDep(Node.right)

        # if leftMinDep == 0:
        #     return rightMinDep + 1
        #
        # if rightMinDep == 0:
        #     return leftMinDep + 1

        return min(leftMinDep, rightMinDep) + 1

#########################
# 此方法和上边的方法是一样的哦，只不过是不是写法更娴熟了一点呢 :)
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

    def isBalanced(self, root: TreeNode):
        if root == None:
            return True

        if abs(self.max_deep(root.left) - self.max_deep(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_deep(self, root):
        if root == None:
            return 0

        return max(self.max_deep(root.left), self.max_deep(root.right)) + 1

##############
# 思考：该方法时间击败了 12.72%的用户，内存击败了 22.22%的用户
# 是否有更好的解决办法呢

if __name__ == "__main__":

    so = Solution1()
    arr = [3,9,20,None,None,15,7]
    # arr = [1,2,2,3,3,None,None,4,4]
    # arr = [3,9,20,10,None,15,7,11]
    root = so.create_tree(arr)
    re = so.isBalanced(root)
    print(re)
    pass