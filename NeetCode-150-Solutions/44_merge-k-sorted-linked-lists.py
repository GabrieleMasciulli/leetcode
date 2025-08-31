"""
Merge K Sorted Linked Lists (Hard):

You are given an array of k linked lists lists, where each list is sorted in ascending order.
Return the sorted linked list that is the result of merging all of the individual linked lists.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        head = node = ListNode()

        # building up the sorted merged list starting with head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if not l2:
            node.next = l1
        if not l1:
            node.next = l2

        return head.next

    def mergeSort(self, arr, left, right):
        head = None

        if left == right:  # one list left, return it
            return arr[left]
        if left > right:
            return None

        mid = left + (right - left) // 2

        head_1 = self.mergeSort(arr, left, mid)
        head_2 = self.mergeSort(arr, mid + 1, right)
        head = self.mergeTwoLists(head_1, head_2)

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeSort(lists, 0, len(lists) - 1)
