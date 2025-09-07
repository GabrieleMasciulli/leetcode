"""
You are given an 2-D array points where points[i] = [xi, yi] represents the
coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.
"""
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-math.sqrt(x**2 + y**2), x, y) for (x, y) in points]
        heapq.heapify(points)

        while len(points) > k:
            heapq.heappop(points)

        return [[x, y] for _, x, y in points]
