"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should
support the following operations


LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the introduction of the new
pair causes the cache to exceed its capacity, remove the least recently used
key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.


"""


class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    Relying only on a hashmap wouldn't satisfy the O(1) time constraint
    on the set operation when the introduction of a new elements causes 
    the cache to exceed its capacity.
    We need a way to quickly access the LRU element such that to replace
    it.

    One way to solve this problem could be using both a hashmap tracking the
    keys currently stored in the cache and a doubly linked list where each
    element points both to the next (more recently used) item and to the
    previous (less recently used) item.

    When the current number of items in the cache doesn't exceed the capacity,
    we simply store the new element after the last node in the list.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.head = Node(0, 0)  # dummy node before LRU node (ptr)
        self.tail = Node(0, 0)  # dummy node before MRU node (ptr)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node):
        """
        Adds a node at the tail of the list.
        """
        last, next = self.tail.prev, self.tail
        last.next = node
        node.prev = last
        next.prev = node
        node.next = next

    def _remove(self, node):
        """
        Remove the specified node from the list.
        """
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _evict(self):
        """
        Removes the LRU node from the list.
        """
        key_to_remove = self.head.next.key
        self._remove(self.head.next)
        self.nodes.pop(key_to_remove, None)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._remove(node)
        self._add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.nodes) == self.capacity:
                self._evict()
            node = Node(key, value)
            self.nodes[key] = node
            self._add(node)
