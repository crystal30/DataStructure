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
    def sortList(self, head: ListNode):
        n = 0
        cur = head
        while cur != None:
            n += 1
            cur = cur.next

        size = 1
        while size < n:
            pass

    def merge(self, cur_i, cur_j):
        temp_head = ListNode(None)
        temp_cur = temp_head

        while cur_i != None or cur_j != None:
            if cur_i.val <= cur_j.val:
                temp_cur.next = cur_i
                cur_i = cur_i.next
                temp_cur = temp_cur.next

            else:
                temp_cur.next = cur_j
                cur_j = cur_j.next
                temp_cur = temp_cur.next

            if cur_i == None and cur_j != None:
                temp_cur.next = cur_j
                break
            elif cur_i != None and cur_j == None:
                temp_cur.next = cur_i
                break

        return temp_head.next

if __name__ == "__main__":
    so = Solution()
    arr1 = [2]
    arr2 = [1]
    head1 = creatLinkedLink(arr1, len(arr1))
    head2 = creatLinkedLink(arr2, len(arr2))
    printLinkedList(head1)
    printLinkedList(head2)
    re = so.merge(head1, head2)
    printLinkedList(re)




