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

class Solution3:
    def pathSum(self, root: TreeNode, sum: int):
        self.path(root, sum, 0, [])

    def path(self, root, sum, level, re):
        if root == None:
            return re

        if root.left == root.right == None:
            if sum == root.val:
                if len(re)==0:
                    re.append([root.val])
                else:
                    re[level] = re[level].append(root.val)
                return re
            else:
                return []

        if len(re)==0:
            re.append([root.val])
        else:
            re[level] = re[level].append(root.val)

        if root.left == None:
            return self.path(root.right, sum-root.val, level+1, re)

        if root.right == None:
            return self.path(root.left, sum-root.val, level+1, re)

        re_l = self.path(root.left, sum - root.val, level + 1, re)
        re_r = self.path(root.right, sum - root.val, level + 1, re)
        return re_l.extend(re_r)


# 求总共有几条路径
class TreeNode1:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from copy import copy
def creat_tree(arr):
    return _create_tree(arr, None, 0)


def _create_tree(arr, root, i):
    if i >= len(arr):
        return None
    if arr[i] == None:
        arr.insert(2 * i + 1, None)
        arr.insert(2 * i + 2, None)
        return None
    root = TreeNode(arr[i])
    root.left = _create_tree(arr, root.left, 2 * i + 1)
    root.right = _create_tree(arr, root.right, 2 * i + 2)
    return root

class Solution2:
    def __init__(self):
        self.all_re = []

    def pathSum(self, root: TreeNode, sum: int):

        self._hasPathSum1(root, sum, [])
        return self.all_re

    def _hasPathSum1(self, root, sum, re):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == sum:
                re.append(root.val)
                self.all_re.append(copy(re))
                return
        re.append(root.val)
        self._hasPathSum1(root.left, sum-root.val, copy(re))
        self._hasPathSum1(root.right, sum-root.val, copy(re))



if __name__ == "__main__":
    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    so = Solution2()
    root = creat_tree(arr)
    re = so.pathSum(root, 22)
    print(re)



