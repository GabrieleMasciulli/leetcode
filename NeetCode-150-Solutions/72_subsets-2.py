"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
The solution must not contain duplicate subsets. You may return the solution in any order.
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(subset, start):
            res.append(subset[:])

            for i in range(start, len(nums)):
                # at least second elem and duplicate number since start
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()

        backtrack([], 0)
        return res
