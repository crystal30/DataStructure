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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        cur = head
        while cur != None:
            length += 1
            cur = cur.next

        if length <=2:
            return head

        cur1 = head
        cur2 = self.cut(head,length//2)
        r_cur2 = self.reverse(cur2)

        while r_cur2 != None:
            cur1_next = cur1.next
            cur1.next = r_cur2

            r_cur2_next = r_cur2.next
            r_cur2.next = cur1_next

            cur1 = cur1_next
            r_cur2 = r_cur2_next

        return head

    def cut(self, head, n):
        # n肯定是有效的
        # 若n=3，可将输入1——>2——>3——>4——>5——>NUll;切分为1——>2——>3——>4——>Null; 5——>NUll

        cur = head
        while n > 0:
            cur = cur.next
            n -= 1

        next = cur.next
        cur.next = None
        return next

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
    arr = [1]

    head = creatLinkedLink(arr, len(arr))
    printLinkedList(head)
    re = so.reorderList(head)
    printLinkedList(re)
