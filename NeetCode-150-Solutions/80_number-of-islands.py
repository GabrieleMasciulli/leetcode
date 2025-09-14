"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and
is surrounded by water. You may assume water is surrounding the grid (i.e., all
the edges are water).
"""


class Solution:
    """
    The idea is to count the number of connected components when treating the
    grid representation as a graph.
    Whenever we encounter a "1" (land) cell when iterating over the grid, we
    add 1 to the island count and apply DFS starting from that cell making
    sure to set any encontered "1" as 0 such that to avoid couting them as
    new islands in later searches.
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == '0':
                return

            grid[row][col] == '0'

            # explore
            for dx, dy in directions:
                dfs(row + dx, col + dy)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
