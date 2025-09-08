"""
Given a 2-D grid of characters board and a string word, return true if the word
is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the
board with horizontally or vertically neighboring cells. The same cell may not
be used more than once in a word.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        ROWS, COLS = len(board), len(board[0])

        def backtrack(row, col, i, visited):
            if i == len(word):
                return True

            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[i] or (row, col) in visited:
                return False

            visited.add((row, col))
            res = backtrack(row, col + 1, i + 1, visited) or\
                backtrack(row, col - 1, i + 1, visited) or\
                backtrack(row - 1, col, i + 1, visited) or \
                backtrack(row + 1, col, i + 1, visited)
            visited.remove((row, col))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0, set()):
                    return True

        return False
