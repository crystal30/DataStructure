# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creatLinkedList(arr, n):
    if n == 0:
        return None

    head = ListNode(arr[0])
    cur = head
    for i in range(1, n):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head

def printLinkedList(head):
    cur = head
    while cur != None:
        print(str(cur.val) + '——>', end='')
        cur = cur.next

    print('Null')

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseLinkedList(l1)
        l2 = self.reverseLinkedList(l2)

        sum_head = ListNode(None)
        sum_cur = sum_head
        temp = 0

        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                sum_cur.val = (l1.val + l2.val + temp) % 10
                temp = (l1.val + l2.val + temp) // 10

                l1 = l1.next
                l2 = l2.next
            elif l1 == None and l2 != None:
                sum_cur.val = (l2.val + temp) % 10
                temp = (l2.val + temp) // 10

                l2 = l2.next
            else:
                sum_cur.val = (l1.val + temp) % 10
                temp = (l1.val + temp) // 10

                l1 = l1.next

            if l1 != None or l2 != None or temp != 0:
                sum_cur.next = ListNode(None)
                sum_cur = sum_cur.next

        if temp != 0:
            sum_cur.val = temp

        return self.reverseLinkedList(sum_head)


    def reverseLinkedList(self, node):
        cur = node
        pre = None

        while cur != None:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        return pre

if __name__ == "__main__":
    so  = Solution()
    arr1 = [7,2,4,3]
    arr2 = [5,6,4]
    l1 = creatLinkedList(arr1, len(arr1))
    printLinkedList(l1)
    l2 = creatLinkedList(arr2, len(arr2))
    printLinkedList(l2)

    re = so.addTwoNumbers(l1,l2)
    printLinkedList(re)


