"""
Given an unsorted array of integers nums and an integer k, return the kth
largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not
the kth distinct element.

Follow-up: Can you solve it without sorting?
"""


import heapq


class Solution:
    """
    This solution has a O(n log k) time complexity where n is the length of nums
    array and k is the size of the heap.

    This solution has a O(k) space complexity where k is the size of the heap.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        i, n = 0, len(nums)

        while i < n:
            heapq.heappush(h, nums[i])
            if len(h) > k:
                print(heapq.heappop(h))
            i += 1
        return h[0]


class Solution2:
    """
    This solution has an average time complexity of O(n) and O(n^2) in the worst
    case, leveraging the quick select algorithm, a slight modification to the
    quick sort algorithm.
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        kTh = 0  # placeholding value

        def partition(arr, left, right):
            i, j = left - 1, left
            pivot = arr[right - 1]  # chosen as the last element

            while j < right:
                # if element at position j is smaller than the pivot then
                # swap elem at position j with elem at position i
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                j += 1

            # finally, swap pivot element in its right place and return correct pivot index
            arr[i + 1], arr[j - 1] = arr[j - 1], arr[i + 1]
            return i + 1

        def quickSort(arr, left, right):
            nonlocal kTh

            if left >= right:
                return

            pivot = partition(arr, left, right)  # idx of the found pivot

            # if pivot is placed at the kTh position, then we found the kTh element
            if pivot == len(arr) - k:
                kTh = nums[pivot]
                return

            # .. else continue with the sorting until the right pivor is found
            quickSort(nums, left, pivot)
            quickSort(nums, pivot + 1, right)

        quickSort(nums, 0, len(nums))

        return kTh
