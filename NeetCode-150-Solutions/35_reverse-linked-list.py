"""
Given the beginning of a singly linked list head, reverse the list, and return
the new beginning of the list.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # inductive step: recursively reverse the rest
        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head
