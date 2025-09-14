"""
Given a 2-D grid of characters board and a list of strings words, return all
words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the
board with horizontally or vertically neighboring cells. The same cell may not
be used more than once in a word.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None


class Solution:
    """
    The idea to solve this problem is to use a Trie data structure to store
    all the words we need to search for and then use this data structure later
    to guide dfs search over the board by pruning paths which are not part of
    any word in the vocabulary.
    """

    def addWordToVocab(self, word, curr):
        for ch in word:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.word = word

    def dfs(self, board, row, ROWS, col, COLS, visited, curr, res):
        if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited:
            return

        ch = board[row][col]
        idx = ord(ch) - ord('a')

        if not curr.children[idx]:
            return

        curr = curr.children[idx]

        if curr.word:
            res.append(curr.word)
            curr.word = None

        visited.add((row, col))

        self.dfs(board, row - 1, ROWS, col, COLS, visited, curr, res)
        self.dfs(board, row + 1, ROWS, col, COLS, visited, curr, res)
        self.dfs(board, row, ROWS, col - 1, COLS, visited, curr, res)
        self.dfs(board, row, ROWS, col + 1, COLS, visited, curr, res)

        visited.remove((row, col))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        vocab = TrieNode()
        res = []

        # first we build the trie data structure (vocabulary) form the given list of words
        for word in words:
            self.addWordToVocab(word, vocab)

        # second we do backtracking search over the board once to find the words in the given list
        for i in range(ROWS):
            for j in range(COLS):
                self.dfs(board, i, ROWS, j, COLS, set(), vocab, res)

        return res
