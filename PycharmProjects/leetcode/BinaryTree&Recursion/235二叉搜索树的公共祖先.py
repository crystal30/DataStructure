# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if p.val > q.val:
            p, q = q, p

        if (root.val >= p.val) and (root.val <= q.val):
            return root

        if (root.val > p.val) and (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)

    # 此种情况不用考虑p,q的大小
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        # p, q均 < 当前节点
        if (root.val > p.val) and (root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        # p, q均 > 当前节点
        if (root.val < p.val) and (root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        # 否则(p或q == root，p q在root的两侧)返回root
        return root.val

    def creat_tree(self, arr):
        return self._creat_tree(arr, None, 0)

    def _creat_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        if arr[i] == None:
            arr.insert(2 * i + 1, None)
            arr.insert(2 * i + 2, None)
            return None

        root = TreeNode(arr[i])
        root.left = self._creat_tree(arr, root, 2 * i + 1)
        root.right = self._creat_tree(arr, root, 2 * i + 2)
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        return self._lowst_common_ancestor(root, min_val, max_val)

    def _lowst_common_ancestor(self, root, min_val, max_val):

        if min_val > root.val:
            return self._lowst_common_ancestor(root.right, min_val, max_val)

        if max_val < root.val:
            return self._lowst_common_ancestor(root.left, min_val, max_val)

        return root

if __name__ == "__main__":
    so = Solution()
    arr = root = [6,2,8,0,4,7,9,None,None,3,5]
    root = so.creat_tree(arr)
    p = TreeNode(2)
    q = TreeNode(8)
    re = so.lowestCommonAncestor2(root, p, q)
    print(re)
