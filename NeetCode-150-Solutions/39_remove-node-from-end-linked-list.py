"""
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> " + self.next.__str__()


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        With a two-pass approach, this problem can be solved by first computing the length
        len of the whole list on a first pass and then removing the (len - n)-th node from 
        the list in a second pass.

        A better approach to only traverse the list once could be using two pointers:
            1. The first which first traverses n nodes starting from the head.
            2. The second which starts from the head too and starts traversing nodes
            one by one simultaneously with the first pointer until the first reaches
            the end of the list. At this point the second node will be exactly at the n-th
            position and the element can be removed.
        """

        first, second = head, head
        i = 0

        # bringing first to n-th position
        while first and i < n:
            first = first.next
            i += 1

        # removing first element of the list
        if not first:
            return head.next

        while first.next:
            second = second.next
            first = first.next

        second.next = second.next.next

        return head
