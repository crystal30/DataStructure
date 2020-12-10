# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        p_isin_left = self.isin(root.left, p)
        p_isin_right = not p_isin_left

        q_isin_left = self.isin(root.left, q)
        q_isin_right = not q_isin_left

        if (p_isin_left and q_isin_right) or (p_isin_right and q_isin_left):
            return root

        if p_isin_left and q_isin_left:
            return self.lowestCommonAncestor(root.left, p, q)

        if p_isin_right and q_isin_right:
            return self.lowestCommonAncestor(root.right, p, q)


    def isin(self, Node, e):
        if Node == None:
            return False

        if Node.val == e.val:
            return True

        return self.isin(Node.left, e) or self.isin(Node.right, e)

class visited_node:
    def __init__(self, node):
        self.node = node
        self.count = 0

from collections import OrderedDict
class Solution:
    def __init__(self):
        self.re_dict = OrderedDict()
        self.count = 0

    def create_tree(self, arr):
        root = self._create_tree(arr, None, 0)
        return root

    def _create_tree(self, arr, root, i):
        if i >= len(arr):
            return None

        if arr[i] == None:
            arr.insert(2*i+1, None)
            arr.insert(2*i+2, None)
            return None
        root = TreeNode(arr[i])
        root.left = self._create_tree(arr, None, 2*i+1)
        root.right = self._create_tree(arr, None, 2*i+2)
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root == None:
            return None
        if root.val == p.val or root.val == q.val:
            self.count += 1

        if self.count == 2:
            re_k = None
            for k,v in self.re_dict.items():
                if v == 2:
                    if k.val == p.val or k.val == q.val:
                        return k
                    re_k = k
            if re_k == None:
                node_list = [e.val for e in self.re_dict.keys()]
                if p.val in node_list:
                    re_k = p
                elif q.val in node_list:
                    re_k = q
                else:
                    pass
            return re_k

        self.re_dict[root] = self.re_dict.get(root, 0)+1
        re_l = self.lowestCommonAncestor(root.left, p, q)
        if re_l != None:
            return re_l
        self.re_dict[root] = self.re_dict.get(root, 0)+1
        re_r = self.lowestCommonAncestor(root.right, p, q)
        self.re_dict[root] = self.re_dict.get(root, 0)+1
        return re_r


    def pre_order(self, root, p, q):
        if root == None:
            return None
        if root.val == p.val or root.val == q.val:
            self.count += 1

        if self.count == 2:
            for k,v in self.re_dict.items():
                if v == 2:
                    return k
        self.re_dict[root] = self.re_dict.get(root, 0)+1
        re_left = self.pre_order(root.left, p, q)
        self.re_dict[root] = self.re_dict.get(root, 0)+1
        re_right = self.pre_order(root.right, p, q)
        self.re_dict[root] = self.re_dict.get(root, 0)+1

        if re_left ==None:
            return re_right
        else:
            return re_left



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Traverse the tree
        self.recurse_tree(root, p, q)
        return self.ans

    def recurse_tree(self, current_node, p, q):

        # If reached the end of a branch, return False.
        if current_node == None:
            return False

        # Left Recursion
        left = self.recurse_tree(current_node.left, p, q)

        # Right Recursion
        right = self.recurse_tree(current_node.right, p, q)

        # If the current node is one of p or q
        mid = current_node == p or current_node == q

        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            self.ans = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right



if __name__ == "__main__":
    arr = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    so = Solution()
    root = so.create_tree(arr)
    p = TreeNode(5)
    q = TreeNode(4)
    re = so.lowestCommonAncestor(root,p, q)
    print(re.val)
    # re = so.pre_order(root, p, q)
    # print(re)