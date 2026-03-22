"""
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)] # dp[i] stores the number of valid ways to decode the string s[i:]

        # base case: empty string can be decoded in one way only:
        dp[n] = 1

        for i in range(n-1, -1, -1): # bottom-up approach
            if s[i] != '0': # add the one-digit only counts
                dp[i] = dp[i + 1]
            if i < n - 1 and (s[i] == '1' or s[i] == '2' and s[i+1] >= '0' and s[i+1] <= '6'):
                dp[i] += dp[i+2]

        return dp[0]
            

