"""
A prefix tree (also known as a trie) is a tree data structure used to
efficiently store and retrieve keys in a set of strings. Some applications of
this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

- PrefixTree() Initializes the prefix tree object.
- void insert(String word) Inserts the string word into the prefix tree.
- boolean search(String word) Returns true if the string word is in the prefix
  tree (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously
  inserted string word that has the prefix prefix, and false otherwise.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False  # used for search operations


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if not node.children[idx]:
                node.children[idx] = TrieNode()

            node = node.children[idx]

        node.isLeaf = True  # marking last char as end of word

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]

            if not node:
                return False
        return node.isLeaf

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')
            node = node.children[idx]

            if not node:
                return False
        return True
