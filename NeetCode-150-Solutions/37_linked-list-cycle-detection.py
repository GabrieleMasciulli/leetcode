"""
Given the beginning of a linked list head, return true if there is a cycle in
the linked list. Otherwise, return false.


There is a cycle in a linked list if at least one node in the list can be
visited again by following the next pointer.


Internally, index determines the index of the beginning of the cycle, if it
exists. The tail node of the list will set it's next pointer to the index-th
node. If index = -1, then the tail node points to null and no cycle exists.


Note: index is not given to you as a parameter.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The idea behind to solve this problem is using the slow and fast pointers
        method i.e. we use 2 pointers:
        - The `slow` pointer moves ahead in the list 1 node at a time
        - The `fast` pointer moves ahead in the list 2 nodes at a time
        If there is a cycle in the linked list, the two pointer will eventually meet
        i.e. the two pointers will have the same reference (not value).
        """
        if not head or not head.next:
            return False
        fast, slow = head.next.next, head

        while fast and fast.next:
            if fast is slow:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
