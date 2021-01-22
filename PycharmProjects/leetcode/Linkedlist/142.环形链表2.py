
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode):
        if head == None:
            return None

        head_nodes = []
        pos = -1
        while head != None:
            if head in head_nodes:
                pos = head_nodes.index(head)
                break
            else:
                head_nodes.append(head)
            head = head.next
        if pos != -1:
            return head_nodes[pos]
        else:
            return None


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    so = Solution()

    re = so.detectCycle(head)
    print("ok")






