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
        record = set()
        cur = head
        pre = None

        while cur != None:
            if cur.val not in record:
                record.add(cur.val)
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                cur.next = None
                cur = pre.next

        return head

if __name__ == "__main__":
    so = Solution()
    arr = [1,1,2,3,3]
    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.deleteDuplicates(head)
    printLinkedList(re)