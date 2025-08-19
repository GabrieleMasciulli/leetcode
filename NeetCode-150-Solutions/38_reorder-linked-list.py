"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> " + self.next.__str__()


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        The intuition behind this problem is that the resulting list can be simply
        formed by merging the first half of the input list with the reversed second
        half.
        To obtain O(n) time and O(1) extra space, we need to modify the elements in place.
        -> This can be done by:
        1. Identifying the middle point of the list such that to know where the reverse 
            operation should begin --> takes O(n / 2) = O(n) time
        2. Reversing the second half. --> takes O(n / 2) = O(n) time
        3. Merging the two portions. --> Takes O(n / 2) = O(n) time

        Total time complexity: 3* O(n/2) = O(n)
        """
        fast, slow = head.next, head

        # find the middle point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        # reverse the second half of the list
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev

        # merge
        while second:
            temp_left, temp_right = first.next, second.next
            first.next = second
            second.next = temp_left
            first = temp_left
            second = temp_right
