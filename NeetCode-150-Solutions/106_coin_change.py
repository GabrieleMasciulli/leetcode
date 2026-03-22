"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.
"""
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([(c, 1) for c in coins]) # (curr_sum, tot_coins_used)
        visited = set() # to avoid exponential blowup of repeated visited states

        if amount == 0:
            return 0

        while queue:
            curr_sum, coins_used = queue.popleft()

            if curr_sum == amount:
                return coins_used

            for c in coins:
                new_sum = curr_sum + c

                if new_sum <= amount and new_sum not in visited:
                    queue.append((new_sum, coins_used + 1))
                    visited.add(new_sum)
            
        return -1