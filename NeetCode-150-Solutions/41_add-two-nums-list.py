"""
You are given two non-empty linked lists, l1 and l2, where each represents a
non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3
-> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not
contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = dummy = ListNode()

        while l1 and l2:
            val = (l1.val + l2.val + carry) % 10
            carry = 1 if (l1.val + l2.val + carry) > 9 else 0
            res.next = ListNode(val)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = (carry + l1.val) % 10
            carry = 1 if (l1.val + carry) > 9 else 0
            res.next = ListNode(val)
            res = res.next
            l1 = l1.next
        while l2:
            val = (carry + l2.val) % 10
            carry = 1 if (l2.val + carry) > 9 else 0
            res.next = ListNode(val)
            res = res.next
            l2 = l2.next

        if carry:
            res.next = ListNode(carry)
            res = res.next

        return dummy.next
