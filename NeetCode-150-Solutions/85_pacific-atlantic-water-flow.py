"""
You are given a rectangular island heights where heights[r][c] represents the
height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders
the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a
neighboring cell with height equal or lower. Water can also flow into the ocean
from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and
Atlantic oceans. Return it as a 2D list where each element is a list [r, c]
representing the row and column of the cell. You may return the answer in any
order.
"""


class Solution:
    """
    Instead of simply running a BFS from each cell, we could consider running
    a DFS from each of the border cells in the opposite way using two separate
    starting sets of coordinates (atlantic and pacific).
    When exploring, we add the neighboring cell to the corresponding set
    which initiated the search and at the end, for each cell we add it to the 
    solutions list if it is in both sets.
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # adding pacific border cells to the set
        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS-1, c))
        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS-1))

        def dfs(r, c, sea):
            for dx, dy in directions:
                if (r+dx, c+dy) not in sea and\
                        r+dx >= 0 and r+dx < ROWS and c+dy >= 0 and\
                        c+dy < COLS and heights[r][c] <= heights[r+dx][c+dy]:
                    sea.add((r+dx, c+dy))
                    dfs(r+dx, c+dy, sea)

        # reverse exploring from all cells in the pacific border
        for r, c in pacific.copy():
            dfs(r, c, pacific)
        pacific = pacific

        for r, c in atlantic.copy():
            dfs(r, c, atlantic)
        atlantic = atlantic

        return list(atlantic.intersection(pacific))
