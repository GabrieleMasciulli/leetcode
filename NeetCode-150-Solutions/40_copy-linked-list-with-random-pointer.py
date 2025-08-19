"""
You are given the head of a linked list of length n. Unlike a singly linked
list, each node contains an additional pointer random, which may point to any
node in the list, or null.


Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node
is represented as a pair of [val, random_index] where random_index is the index
of the node (0-indexed) that the random pointer points to, or null if it does
not point to any node.

"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        The problem here is that we are not able to deepcopy the original
        list as we traverse it without storing any additional information 
        because whenever we encounter a new pointer which we had previously
        not found we cannot reference it in the new array as the new one
        doesn't exist yet.

        A solution can be to store in a hashmap all the original pointers
        as keys as the list is traversed and the corresponding deep copied
        node as value.
        Then, with a second pass, all the random (deep copied) pointers can
        be easily referenced as they were already created and stored in the
        hashmap.
        """
        if not head:
            return head

        curr = head
        ptr_map = {}

        # build a mapping between the pointers in the input list
        # and the deep copies.
        while curr:
            ptr_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = ptr_map[curr]
            if curr.next:
                next_copy = ptr_map[curr.next]
                copy.next = next_copy
            if curr.random:
                random_copy = ptr_map[curr.random]
                copy.random = random_copy
            curr = curr.next

        return ptr_map[head]  # returing the new head
