from copy import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        re = []
        return self.pathS(root, sum, re)

    def pathS(self, Node, sum, re):
        if Node == None:
            return []

        if re == []:
            re.append([Node.val])
        else:
            re[-1].append(Node.val)

        if Node.left == Node.right == None:
            if Node.val == sum:
                return re
            else:
                return []

        re_l = [e.copy() for e in re]
        re_r = [e.copy() for e in re]
        re_l = self.pathS(Node.left, sum - Node.val, re_l)
        re_r = self.pathS(Node.right, sum - Node.val, re_r)
        re_l.extend(re_r)

        return re_l

class Solution1:
    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, sum: int):
        if root == None:
            return self.res

        self._path_sum(root, sum, []) # 检测当root == None时
        return self.res

    def _path_sum(self, root, sum, path_list):
        if root == None:# 思考，如果都是正数，这里可以让sum=0时候也停止
            if sum == 0:
                self.res.append(path_list)
            return

        sum -= root.val
        path_list.append(root.val)

        if root.left == None:
            self._path_sum(root.right, sum, copy(path_list))
        elif root.right == None:
            self._path_sum(root.left, sum, copy(path_list))
        else:
            self._path_sum(root.left, sum, copy(path_list))
            self._path_sum(root.right, sum, copy(path_list))

        return

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    so = Solution1()
    re = so.pathSum(root, 22)
    print(re)



