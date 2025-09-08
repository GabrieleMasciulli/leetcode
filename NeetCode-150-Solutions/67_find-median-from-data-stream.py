"""
The median is the middle value in a sorted list of integers. For lists of even
length, there is no middle value, so the median is the mean of the two middle
values.

For example:
- For arr = [1,2,3], the median is 2.
- For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far.
"""
import heapq


class MedianFinder:
    """
    The idea behind this solution comes from the fact that, given a sorted
    array, when dividing it into two halves, the median value in the case of
    an even number of elements corresponds to the max of the first half + the
    min of the second half divided by two. In the case of an odd number of elements
    the median corresponds to the max value of the first half if it has the most
    number of elements, otherwise the min number of the second half.

    To implement this idea, we can leverage  max heap and a min heap to keep
    track of the two parts of the array while adding elements one by one.
    There are two things to consider:
    - The two heaps must be kept balanced while adding new elements
    - The two heaps must be kept consistent with each other i.e., each
    the one handling the left portion of the array should keep those elements
    only, and the same goes for the right side.

    The max heap is going to store the left side of the array, while the
    min heap is going to store the right side of the array.
    """

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # always push to the min heap first ...
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # ... then re-balance heaps if unbalanced
        m, n = len(self.maxHeap), len(self.minHeap)

        if n > m + 1:  # min heap has more than one elem difference from max heap
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        if m > n + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        n, m = len(self.minHeap), len(self.maxHeap)

        # even case -> return mean between max of left and min of right
        if n == m and n + m > 1:
            el1 = -self.maxHeap[0]
            el2 = self.minHeap[0]
            return (el1 + el2) / 2

        if n > m:  # return elem at the top of min heap
            return self.minHeap[0]

        return -self.maxHeap[0]
