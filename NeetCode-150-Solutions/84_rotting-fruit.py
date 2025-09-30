"""
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a
rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh
fruits remaining. If this state is impossible within the grid, return -1.
"""

from collections import deque


class Solution:
    """
    The idea to solve this problem coul be to first save the locations of all
    the rotten fruits by adding them to a queue.
    Then, we start a multi-source DFS from the rotten fruit locations
    simulataneously and at each iteration mark the adjacent fruits as
    rotten too making also keeping track of the minutes elapsed.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        fruit_count = 0

        # first we search for the rotten fruits
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))  # adding cell to the queue
                if grid[i][j] == 1:
                    fruit_count += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        elapsed = 0
        found_fresh = 0

        while q:
            elems = len(q)

            for i in range(elems):
                row, col = q.popleft()

                for dx, dy in directions:
                    if (row + dx) >= 0 and (row + dx) < ROWS and (col + dy) >= 0 and (col + dy) < COLS and grid[row+dx][col+dy] == 1:
                        found_fresh += 1
                        grid[row+dx][col+dy] = 2
                        q.append((row+dx, col+dy))
            if q:
                elapsed += 1

        return elapsed if found_fresh == fruit_count else -1
