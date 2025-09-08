"""
You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the
chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two
combinations are the same if the frequency of each of the chosen numbers is the
same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in
each combination can be in any order.
"""


class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(elems, s, start):
            if s == target:
                res.append(elems[:])
            elif s > target:
                return  # overflow -> stop search

            for i in range(start, len(nums)):
                elems.append(nums[i])

                # passing `i` as start such that to generate subsets with the same element
                # contained multiple times. Avoids using past elements.
                backtrack(elems, s + nums[i], i)

                elems.pop()

        backtrack([], 0, 0)
        return res
