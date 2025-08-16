class Solution:
    """
    You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

    Return the area of the largest rectangle that can be formed among the bars.

    Note: This chart is known as a histogram.

    Example 1:

    Input: heights = [7,1,7,2,2,4]

    Output: 8
    Example 2:

    Input: heights = [1,3,7]

    Output: 7
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        # contains the index of the first encountered bar at the left smaller than the current bar
        leftClosest = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftClosest[i] = stack[-1]
            stack.append(i)

        stack = []
        # contains the index of the first encountered bar at the right smaller than the current bar
        rightClosest = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightClosest[i] = stack[-1]
            stack.append(i)

        max_area = 0

        for i in range(n):
            width = rightClosest[i] - leftClosest[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
