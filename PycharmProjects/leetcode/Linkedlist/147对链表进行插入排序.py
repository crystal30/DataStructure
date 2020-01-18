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
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        if head != None:
            cur = head.next
            head.next = None

            while cur != None:
                p = dummy_head
                while p.next != None and p.next.val <= cur.val:
                    p = p.next

                # p.next.val > cur.val
                temp = cur.next
                cur.next = p.next
                p.next = cur

                cur = temp

        return dummy_head.next

if __name__ == "__main__":
    so = Solution()
    arr = [6,5,3,1,8,7,2,4]
    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.insertionSortList(head)
    printLinkedList(re)
