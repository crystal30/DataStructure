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
    def oddEvenList(self, head: ListNode) -> ListNode:
        pre = head
        if head == None:
            return head
        cur = head.next
        i = 2

        while cur != None:
            next = cur.next
            if i % 2 == 0 and next != None:

                cur.next = next.next
                next.next = pre.next
                pre.next = next

                pre = pre.next
            else:
                cur = next

            i += 1

        return head

if __name__ == "__main__":
    so = Solution()
    nums = [2,1,3,5,6,4,7]
    head = creatLinkedLink(nums, len(nums))
    printLinkedList(head)
    re = so.oddEvenList(head)
    printLinkedList(re)



