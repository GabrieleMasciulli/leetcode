"""
Given an array nums of unique integers, return all the possible permutations.
You may return the answer in any order.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, picked):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if not picked[i]:
                    curr.append(nums[i])
                    picked[i] = True
                    backtrack(curr, picked)
                    curr.pop()
                    picked[i] = False

        backtrack([], [False] * len(nums))
        return res
