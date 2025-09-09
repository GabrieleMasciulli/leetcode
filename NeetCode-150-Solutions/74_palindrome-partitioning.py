"""
Given a string s, split s into substrings where every substring is a palindrome.
Return all possible lists of palindromic substrings.

You may return the solution in any order.
"""


class Solution:
    """
    Given a string s, there are 2^n possible partitions.
    If, we generate all possible partitions the for each one
    we can check if it is a palindrome partition or not and
    add it to the resulting list of palindrome partitions.
    """

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(substr):
            l, r = 0, len(substr) - 1

            while l <= r:
                if substr[l] != substr[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(substrings, idx):
            if idx >= len(s):
                res.append(substrings.copy())
                return

            for i in range(idx, len(s)):
                if isPalindrome(s[idx: i + 1]):
                    substrings.append(s[idx: i + 1])

                    backtrack(substrings, i + 1)

                    substrings.pop()

        backtrack([], 0)
        return res
