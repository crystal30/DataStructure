# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        dummy_head = ListNode(None)
        dummy_head.next = node

        pre = dummy_head
        while node.next != None:
            node.val = node.next.val
            pre = node
            node = node.next

        pre.next = None


    def deleteNode1(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 由于node不是最后一个节点，故 node.next.val 恒有值
        node.val = node.next.val
        node.next = node.next.next
