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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = None
        cur = head

        while cur != None:
            if cur.val == val:
                if pre == None:
                    head = cur.next
                else:
                    pre.next = cur.next

                cur = cur.next
            else:
                pre = cur
                cur = cur.next

        return head

if __name__ == "__main__":
    so = Solution()
    arr = [1,1,6,3,4,5,6]
    val = 1
    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.removeElements(head, val)
    printLinkedList(re)

