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

    for i in range(1,n):
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
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next

        if length <= 1:
            return True

        cur1 = head
        cur2 = self.cut(head, length//2)
        r_cur2 = self.reverse(cur2)

        while r_cur2 != None:
            if r_cur2.val != cur1.val:
                return False
            else:
                r_cur2 = r_cur2.next
                cur1 = cur1.next

        return True


    def cut(self, head, n):
        cur = head
        while n > 0:
            cur = cur.next
            n -= 1

        return cur

    def reverse(self, head):
        pre = None
        cur = head

        while cur != None:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        return pre

if __name__ == "__main__":
    so = Solution()
    arr = [1,2,3,2,1]
    head = creatLinkedList(arr, len(arr))
    printLinkedList(head)

    re = so.cut(head, 2)
    printLinkedList(re)
    re1 = so.reverse(re)
    printLinkedList(re1)