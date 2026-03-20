"""
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j] == True -> s[i:j+1] is palindrome
        palCount = 0

        for i in range(n-1, -1, -1): # from end to start
            for j in range(i, n): # from i to end
                isPal = s[i] == s[j]

                if isPal and (j - i + 1 <= 2 or dp[i+1][j-1]):
                    palCount += 1    
                    dp[i][j] = True

        
        return palCount
