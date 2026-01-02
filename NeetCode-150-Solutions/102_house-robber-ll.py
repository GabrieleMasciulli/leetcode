"""
You are given an integer array nums where nums[i] represents the amount of money the ith house has.
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security
system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
"""


def aux(nums):
    n = len(nums)

    if not nums:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(aux(nums[1:]), aux(nums[:-1]))
