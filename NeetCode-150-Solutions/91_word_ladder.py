"""
You are given two words, beginWord and endWord, and also a list of words wordList.
All of the given words are of the same length, consisting of lowercase English letters,
and are all distinct.

Your goal is to transform beginWord into endWord by following the rules:

You may transform beginWord to any word within wordList, provided that at exactly
one position the words have a different character, and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed
to obtain the endWord, or 0 if no such sequence exists.
"""

from collections import deque


class Solution:
    """
    The idea to solve this problem is to start from the beginWord
    and generate all possible words which differ by one char with it
    via a BFS algorithm.
    Example:
    - Given the word `bat` we can generate the following words:
        1. all words as `*at` i.e. `aat`, `bat`(skip), `cat` .. `zat`
        2. all words as `b*t` i.e. `bat`(skip), `bbt`, `bct` .. `bzt`
        3. and all words as `ba*` i.e. `baa`, `bab`, `bac` .. `baz`
    ... the generated word is added to a queue if it's present in
    the list of words passed as input.
    When popping words from the queue we keep track of the number of
    "hops" and when the popped word matches the endWord then we
    simply return the number of "hops" taken, otherwise zero.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if (endWord not in words) or beginWord == endWord:
            return 0

        m = len(beginWord)
        q = deque([beginWord])
        res, visited = 0, set()

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(m):  # iterating over all word indices
                    for j in range(
                        ord("a"), ord("z") + 1
                    ):  # iterating over all possible chars
                        if chr(j) == word[i]:
                            continue
                        new_word = word[:i] + chr(j) + word[i + 1 :]

                        if new_word in words and new_word not in visited:
                            visited.add(new_word)
                            q.append(new_word)
        return 0
