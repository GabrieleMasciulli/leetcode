"""
You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next
k nodes, and so on. If there are fewer than k nodes left, leave the nodes as
they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)

        while groupPrev.next:
            kTh = self.getKth(groupPrev, k)
            if not kTh:
                break

            groupNext = kTh.next
            prev, curr = kTh.next, groupPrev.next

            # reversing list, starting from head of current group
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kTh
            groupPrev = tmp

        return dummy.next

    def getKth(self, start, k):
        """
        Returns the k-th element starting from the input node
        """
        i, curr = 0, start
        while curr and i < k:
            curr = curr.next
            i += 1
        return curr
