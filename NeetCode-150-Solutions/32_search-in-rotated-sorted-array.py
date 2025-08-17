class Solution:
    """
    You are given an array of length n which was originally sorted in ascending order.
    It has now been rotated between 1 and n times.

    For example, the array nums = [1,2,3,4,5,6] might become:
    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.
    Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

    You may assume all elements in the sorted rotated array nums are unique,

    A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
