"""
Design a class to find the kth largest integer in a stream of values, including
duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not
necessarily sorted.

Implement the following methods:
- constructor(int k, int[] nums) Initializes the object given an integer k and
the stream of integers nums.
- int add(int val) Adds the integer val to the stream and returns the kth
  largest integer in the stream.
"""
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        # removing elements from heap until only K elements remain
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # kTh largest is already the min in the heap as it only stores k elements
        return self.heap[0]
