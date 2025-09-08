"""
Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution
in any order.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            nonlocal res

            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                # create new subsets starting keeping the current path as fixed
                backtrack(i + 1, path)

                # undo last choice
                path.pop()

        backtrack(0, [])
        return res
