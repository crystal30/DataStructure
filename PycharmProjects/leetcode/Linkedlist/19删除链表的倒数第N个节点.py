# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 通过list创建链表
def creatLinkedLink(arr, n):
    if n == 0:
        return None

    head = ListNode(arr[0])
    cur = head

    for i in range(1, n):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

# 打印链表
def printLinkedList(head):
    cur = head
    while cur != None:
        print(str(cur.val) + '——>', end='')
        cur = cur.next

    print('Null')

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        cur = head
        length = 0
        while cur != None:
            length += 1
            cur = cur.next

        dummy_head = ListNode(0)
        dummy_head.next = head

        cur = dummy_head
        length += 1

        while cur != None:
            pre = cur
            cur = cur.next
            length -= 1

            if length == n:
                # 此时cur即为要删除的节点。由于其保证 n是有效的。故cur != None
                pre.next = cur.next
                cur.next = None

        return dummy_head.next

    # 只遍历一次
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode(0)
        dummy_head.next = head

        p = dummy_head # 为要删除节点的前一个节点
        cur = head
        while n > 0: # 由于其给出的节点n是有效的，故在这里 cur ！= None
            cur = cur.next
            n -= 1

        q = cur

        while q != None:
            p = p.next
            q = q.next

        p.next = p.next.next  # 同样由于其给出的节点n是有效的，p.next != None,不可能删除倒数第0个节点

        return dummy_head.next

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,4,5]
    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.removeNthFromEnd1(head, 5)
    printLinkedList(re)
