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

    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        if cur == None or cur.next == None:
            return head

        next = cur.next
        cur.next = None

        pre = cur
        cur = next

        while cur.next != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        cur.next = pre

        return cur

if __name__ == "__main__":
    so = Solution()
    for i in [1,2,3,4,5]:
        so.add(i)
    re = so.reverseList(so.head)
    pass


