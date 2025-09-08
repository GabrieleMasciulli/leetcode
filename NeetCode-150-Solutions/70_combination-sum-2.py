"""
You are given an array of integers candidates, which may contain duplicates, and
a target integer target. Your task is to return a list of all unique
combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination.
The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(subset, s, start):
            if s == target:
                res.append(subset[:])
                return
            if s > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                subset.append(candidates[i])

                backtrack(subset, s + candidates[i], i + 1)

                subset.pop()

        backtrack([], 0, 0)
        return res
