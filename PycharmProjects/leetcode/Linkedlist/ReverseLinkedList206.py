# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0

    def add(self, e):
        cur = self.head
        if cur.val == None:
            cur.val = e
            self.size += 1
        else:
            while cur.next != None:
                cur = cur.next

            cur.next = ListNode(e)
            self.size += 1

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prv = None
        cur = head
        if cur != None and cur.next != None:
            af = cur.next
        else:
            return head
        while af.next != None:
            cur.next = prv
            prv = cur
            cur = af
            af = af.next

        cur.next = prv
        af.next = cur
        return af

    #对reverseList的步骤进行精简
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prv = None
        cur = head
        while cur != None:
            af = cur.next
            cur.next = prv
            prv = cur
            cur = af

        return prv

if __name__ == "__main__":
    so = Solution()
    for i in [1,2,3,4,5]:
        so.add(i)
    re = so.reverseList1(so.head)
    pass





