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
    def partition(self, head: ListNode, x: int) -> ListNode:
        n_head = ListNode(None) # 虚拟头节点
        n_head.next = head

        pre = n_head
        cur = head

        Node_cur = cur
        Node_pre = pre

        while cur != None:
            if cur.val >= x:
                pre = cur
                cur = cur.next

            else:
                if Node_pre == pre and Node_cur == cur:
                    pre = cur
                    cur = cur.next
                    Node_pre = pre
                    Node_cur = cur
                else:
                    pre.next = cur.next
                    cur.next = Node_cur
                    Node_pre.next = cur

                    Node_pre = cur

                    cur = pre.next

        return n_head.next

if __name__ == "__main__":
    so = Solution()
    nums = [2,1]
    head = creatLinkedLink(nums, len(nums))
    printLinkedList(head)
    re = so.partition(head, 2)
    printLinkedList(re)
