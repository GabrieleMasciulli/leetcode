"""
You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may
return the answer in any order.
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        if not digits:
            return res

        def dfs(comb, idx):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            digit = digits[idx]
            letters = letterMap[digit]

            # for each letter mapped to the digit at the current posiiton 'idx'
            for i in range(len(letters)):
                comb.append(letters[i])

                dfs(comb, idx + 1)

                comb.pop()

        dfs([], 0)
        return res
