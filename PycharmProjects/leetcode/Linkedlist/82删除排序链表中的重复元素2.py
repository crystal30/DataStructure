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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        cur = head
        record = set()
        remove_r = set()
        while cur != None:
            if cur.val not in record:
                record.add(cur.val)
                pre = cur
                cur = cur.next
            else:
                remove_r.add(cur.val)
                cur = cur.next
                pre.next = cur

        cur = head
        pre = dummy_head
        while cur != None:
            if cur.val in remove_r:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next

        return dummy_head.next

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,3,3,4,4,5]
    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.deleteDuplicates(head)
    printLinkedList(re)



