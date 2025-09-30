"""
You are given an integer n representing the number of steps to reach the top of
a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n

        if n <= 2:
            return n

        dp[0], dp[1] = 1, 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n-1]
