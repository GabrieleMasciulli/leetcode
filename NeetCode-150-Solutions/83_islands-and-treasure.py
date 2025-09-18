"""
You are given a 
m x n 2D grid initialized with these three possible values:
- -1 - A water cell that can not be traversed.
- 0 - A treasure chest.
- INF - A land cell that can be traversed. We use the integer 2^31 - 1 =
2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land
cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.


"""
from collections import deque


class Solution:
    """
    The idea is that instead of running a BFS from each land cell such that to
    find the closest treasure chest, we can approach the problem in the reverse 
    process i.e., we run DFS for each treasure chest for each level.
    Whenever we encouter a land cell, we mark it with the current path cost for 
    reaching that cell if it improves the previous best path cost for reaching it.
    """

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque([])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        # initially we only add the treasure cells to the queue
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        distance = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                grid[row][col] = distance

                for dx, dy in directions:
                    if (row + dx) < 0 or (row + dx) >= m or (col + dy) < 0 or (col + dy) >= n or grid[row + dx][col + dy] == -1 or (row + dx, col + dy) in visited:
                        continue

                    q.append((row + dx, col + dy))
                    visited.add((row + dx, col + dy))
            distance += 1
