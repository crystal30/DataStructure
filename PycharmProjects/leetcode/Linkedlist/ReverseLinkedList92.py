class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self,e):

        if self.head == None:
            self.head = ListNode(e)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = ListNode(e)
        self.size += 1

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prv = ListNode(None)
        prv.next = head
        cur = head
        for _ in range(m-1): #0,1
            af = cur.next
            prv = cur
            cur = af
        h = prv
        af = cur.next
        for _ in range(n-m):#n-m=2; 取值0，1
            prv = cur
            cur = af
            af = cur.next
            cur.next = prv
        h.next.next = af
        h.next = cur
        if h.val == None:
            return h.next
        else:
            return head

if __name__ == "__main__":
    # 1->2->3->4->5->NULL, m = 2, n = 4
    # 1->4->3->2->5->NULL
    so = Solution()
    for e in [1,2,3,4,5]:
        so.add(e)
    re = so.reverseBetween(so.head, 2, 4)
    pass
