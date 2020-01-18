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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_cur = l1
        l2_cur = l2
        sum_head = ListNode(None)
        sum_cur = sum_head
        temp = 0

        while l1_cur != None and l2_cur != None:
            sum_cur.val = (l1_cur.val + l2_cur.val + temp) % 10
            temp = (l1_cur.val + l2_cur.val + temp) // 10

            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
            if l1_cur != None or l2_cur != None or temp != 0:
                sum_cur.next = ListNode(None)
                sum_cur = sum_cur.next

        while l2_cur != None:
            sum_cur.val = (l2_cur.val + temp) % 10
            temp = (l2_cur.val + temp) // 10

            l2_cur = l2_cur.next

            if l2_cur != None or temp != 0:
                sum_cur.next = ListNode(None)
                sum_cur = sum_cur.next

        while l1_cur != None:
            sum_cur.val = (l1_cur.val + temp) % 10
            temp = (l1_cur.val + temp) // 10

            l1_cur = l1_cur.next

            if l1_cur != None or temp != 0:
                sum_cur.next = ListNode(None)
                sum_cur = sum_cur.next

        if temp != 0:
            sum_cur.val = temp

        return sum_head


if __name__ == "__main__":
    so = Solution()
    arr1 = [2,4,3,1]
    arr2 = [5,6,4]

    l1 = creatLinkedLink(arr1, len(arr1))
    l2 = creatLinkedLink(arr2, len(arr2))

    printLinkedList(l1)
    printLinkedList(l2)

    re = so.addTwoNumbers(l1, l2)
    printLinkedList(re)



