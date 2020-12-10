# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creatLinkedList(arr, n):
    if n == 0:
        return None
    head = ListNode(arr[0])
    cur_Node = head
    for i in range(1,n):
        cur_Node.next = ListNode(arr[i])
        cur_Node = cur_Node.next

    return head

def printLinkedList(head):
    cur = head
    while cur != None:
        print(str(cur.val) + '——>', end='')
        cur = cur.next

    print('Null')

class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = None
        cur = head
        Node_pre = pre
        Node_cur = cur
        index = 1

        while index != n+1:
            next = cur.next
            if index == m:
                Node_pre = pre
                Node_cur = cur

            elif index > m and index <= n:
                cur.next = pre
            pre = cur
            cur = next
            index += 1

        if m == 1:
            Node_cur.next = cur
            return pre
        else:
            Node_pre.next = pre
            Node_cur.next = cur

            return head


if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,4,5]
    head = creatLinkedList(nums, len(nums))
    printLinkedList(head)
    m = 2
    n = 5

    re = so.reverseBetween(head, m, n)
    printLinkedList(re)
    pass