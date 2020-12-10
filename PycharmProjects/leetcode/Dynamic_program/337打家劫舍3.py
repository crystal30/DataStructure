# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init__(self):
    #     self.res = [0]
    # def create_tree(self, arr):
    #     len_arr = len(arr)
    #     return self._create_tree(arr, len_arr, 0, None)
    #
    # def _create_tree(self, arr, len_arr, i, root):
    #     if i >= len_arr:
    #         return None
    #
    #     if arr[i] == None:
    #         arr.insert(2*i+1, None)
    #         arr.insert(2*i+2, None)
    #         return None
    #
    #     root = TreeNode(arr[i])
    #     root.left = self._create_tree(arr, len_arr, 2*i+1, root.left)
    #     root.right = self._create_tree(arr, len_arr, 2 * i + 2, root.right)
    #     return root

    def rob(self, root):
        return self.try_rob(root)


    def try_rob(self, root):
        if root == None:
            return 0

        root_val = root.val
        if root.left == None and root.right == None:
            return root.val
        res = -1
        if root.left == None:
            return max(res, root_val + self.try_rob(root.right.left) + self.try_rob(root.right.right))

        if root.right == None:
            return max(res, root_val + self.try_rob(root.left.left) + self.try_rob(root.left.right))


        return max(res, root_val + self.try_rob(root.left.left)+ self.try_rob(root.left.right)\
                        + self.try_rob(root.right.left) + self.try_rob(root.right.right))

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def arr_to_tree(arr_list):
    if len(arr_list) == 0:
        return None
    return _arr_to_tree(0, arr_list, None)

def _arr_to_tree(i, arr_list, root):
    if i >= len(arr_list):
        return None

    root = TreeNode(arr_list[i])
    if arr_list[i] == None:
        arr_list.insert(2*i+1, None)
        arr_list.insert(2*i+2, None)
        return None

    root.left = _arr_to_tree(2*i+1, arr_list, root)
    root.right = _arr_to_tree(2*i+2, arr_list, root)
    return root

class Solution5:
    def __init__(self):
        self.memo = dict()
    def rob(self, root):
        if root == None:
            return 0
        return self._rob(root)


    # root 这颗树中，可以偷取的最大金额
    def _rob(self, root):
        if root in self.memo.keys():
            return self.memo[root]

        if root == None:
            self.memo[root] = 0

        # 既没有左子树，又没有右子树
        elif root.left == None and root.right == None:
            self.memo[root] = root.val

        # 只有左子树
        elif root.left != None and root.right == None:
            self.memo[root] = max([root.val + self._rob(root.left.left) + self._rob(root.left.right),
            self._rob(root.left)])


        # 只有右子树
        elif root.left == None and root.right != None:
            self.memo[root] = max([root.val + self._rob(root.right.left) + self._rob(root.right.right),
                                  self._rob(root.right)])

        # 既有左子树，又有右子树
        else:
            self.memo[root] = max([root.val + self._rob(root.left.left) + self._rob(root.left.right) + self._rob(root.right.left) + self._rob(root.right.right),
            self._rob(root.left) + self._rob(root.right.left) + self._rob(root.right.right),
            self._rob(root.right) + self._rob(root.left.left) + self._rob(root.left.right),
            self._rob(root.left) + self._rob(root.right)])

        return self.memo[root]



if __name__ == "__main__":
    so = Solution5()
    # arr = [3,2,3,None,3,None,1]
    arr = [3,2,3,None,3,None,1]
    root = arr_to_tree(arr)
    re = so.rob(root)
    print(re)

