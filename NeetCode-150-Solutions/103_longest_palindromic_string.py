"""
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestIdx = 0  # starting index of the longest resulting palindrome substring
        longestLen = 0  # length of the longest resulting palindrome substring

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                isPalindrome = s[i] == s[j]

                if isPalindrome and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > longestLen:
                        longestLen = j - i + 1
                        longestIdx = i

        return s[longestIdx : longestIdx + longestLen]
