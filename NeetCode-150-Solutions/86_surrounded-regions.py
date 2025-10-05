"""
You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by
'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.
"""


class Solution:
    """
    The idea to solve this problem is to solve it in the reverse order
    i.e. starting from the edge/corner cells, we mark all O cells as
    "safe" if they are connected to an edge or a O cell already marked as safe.
    All remaining O's will be marked as X
    """

    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        borders = set()
        safe = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # adding all 'O' border cells to start the DFS with
        for r in range(ROWS):
            if board[r][0] == 'O':
                borders.add((r, 0))
            if board[r][COLS-1] == 'O':
                borders.add((r, COLS-1))

        for c in range(COLS):
            if board[0][c] == 'O':
                borders.add((0, c))
            if board[ROWS-1][c] == 'O':
                borders.add((ROWS-1, c))

        def dfs(r, c):
            nonlocal safe

            safe.add((r, c))

            for dx, dy in directions:
                if dx+r >= 0 and dx+r < ROWS and dy+c >= 0 and dy+c < COLS and (dx+r, dy+c) not in safe and board[dx+r][dy+c] == 'O':
                    dfs(dx+r, dy+c)

        # running dfs from adge O's
        for r, c in borders:
            dfs(r, c)

        # marking all unsafe O's as X's
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe and board[r][c] == 'O':
                    board[r][c] = 'X'
