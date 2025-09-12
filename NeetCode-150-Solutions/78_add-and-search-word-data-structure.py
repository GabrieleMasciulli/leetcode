"""
Design a data structure that supports adding new words and searching for
existing words.

Implement the WordDictionary class:
- void addWord(word) Adds word to the data structure.
- bool search(word) Returns true if there is any string in the data structure that
matches word or false otherwise. word may contain dots '.' where dots can be
matched with any letter.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
        curr.isLeaf = True

    def search(self, word: str) -> bool:

        def searchRecursive(curr, idx):
            nonlocal word

            if not curr:
                return False
            if idx == len(word):
                return curr.isLeaf

            if word[idx] == '.':
                for child in curr.children:
                    if searchRecursive(child, idx + 1):
                        return True
                return False
            else:
                ch = word[idx]
                return searchRecursive(curr.children[ord(ch) - ord('a')], idx + 1)

            return curr.isLeaf

        return searchRecursive(self.root, 0)
