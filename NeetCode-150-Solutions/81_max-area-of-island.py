"""
You are given a matrix grid where grid[i] is either a 0 (representing water) or
1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You
may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        The idea to solve this problem is to treat the grid as a graph and
        whenever a "1" is found, a DFS is begins which recursively looks
        for nearby land cells and keeps the count of connected land cells.
        """
        maxArea = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0

            area = 1

            # current cell is a land, explore

            grid[row][col] = 0

            for dx, dy in directions:
                area += dfs(row + dx, col + dy)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(dfs(i, j), maxArea)

        return maxArea
