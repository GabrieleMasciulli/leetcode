import math


class Solution:
    """
    You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
    You are also given an integer h, which represents the number of hours you have to eat all the bananas.

    You may decide your bananas-per-hour eating rate of k.
    Each hour, you may choose a pile of bananas and eats k bananas from that pile.
    If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

    Return the minimum integer k such that you can eat all the bananas within h hours.


    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        - Given the fact that h is always greater than or equal to the length
        of the piles, the upperbound for the rate at which Koko eats the bananas
        corresponds to the largest value of bananas in the piles.
            -> In this scenario, given k = max(piles) then Koko takes
            len(piles) hours to eat all the bananas.

        - Because of this constraint, instead of linearly searching the minimum
        k in range (1, max(piles)) and check at each iteration if the time constraint
        is being satisfied, we binary search k in the same range reducing the time
        complexity from O(n * m) to O(n log m)
        """
        l, r = 1, max(piles)
        smallest_k = r

        while l <= r:
            k = l + (r - l) // 2

            # check if current k satisfies the time constraints
            hours_left = h

            i = 0
            while i < len(piles):
                time_to_eat = math.ceil(piles[i] / k)
                hours_left -= time_to_eat
                i += 1

            if hours_left >= 0:  # k might be decreased
                smallest_k = min(smallest_k, k)
                r = k - 1
            else:  # need to increase k
                l = k + 1

        return smallest_k
