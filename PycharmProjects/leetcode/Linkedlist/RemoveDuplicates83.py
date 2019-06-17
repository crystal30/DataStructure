# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head = None

    def add(self, arr):
        for e in arr:
            if self.head == None:
                self.head = ListNode(e)
                cur = self.head
            else:
                cur.next = ListNode(e)
                cur = cur.next

    #52ms, 但感觉程序有点冗长
    #时间复杂度：？
    #空间复杂度：？
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        # 当head != None时
        prv = head
        cur = prv.next
        while cur != None:
            while cur != None and cur.val == prv.val:
                prv.next = cur.next
                cur.next = None
                cur = prv.next
            if cur == None:
                return head
            prv = cur
            cur = prv.next
        return head



if __name__ == "__main__":
    # 1->1->2->3->3
    so = Solution()
    so.add([1,1,1])
    re = so.deleteDuplicates(so.head)
    pass