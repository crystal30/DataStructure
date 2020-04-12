# Definition for singly-linked list.
from queue import PriorityQueue
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def creatLinkedList(arr, n):
    if n == 0:
        return None
    root = ListNode(arr[0])
    node = root
    for i in range(1, n):
        node.next = ListNode(arr[i])
        node = node.next

    return root

class Solution:
    def mergeKLists(self, lists):
        pq = PriorityQueue()
        for listNode in lists:
            node = listNode
            while node != None:
                pq.put(node.val)
                node = node.next

        if pq.qsize() >= 1:
            root = ListNode(pq.get())
            node = root
            while pq.qsize() > 0:
                node.next = ListNode(pq.get())
                node = node.next

            return root
        else:
            return None

# 注意语言的简练，不冗余

if __name__ == "__main__":
    so = Solution()
    arr1 = [1,4,5]
    arr2 = [1,3,4]
    arr3 = [2,6]
    lists = [creatLinkedList(arr1, len(arr1)), creatLinkedList(arr2, len(arr2)),
             creatLinkedList(arr3, len(arr3))]
    re = so.mergeKLists(lists)
    pass



