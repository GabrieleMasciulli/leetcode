class Solution:
    """
    You are given an array of length n which was originally sorted in ascending order.
    It has now been rotated between 1 and n times.

    For example, the array nums = [1,2,3,4,5,6] might become:
    [3,4,5,6,1,2] if it was rotated 4 times.
    [1,2,3,4,5,6] if it was rotated 6 times.

    Notice that rotating the array 4 times moves the last four elements of the array to the beginning.
    Rotating the array 6 times produces the original array.

    Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

    A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
    """

    def findMin(self, nums: List[int]) -> int:
        """
        The idea is that if the array was rotated less than n times,
        then the first element of the array will always be bigger than 
        the last element of the array.
        Then, we can binary search the array by iteratively searching the minimum
        in the portion of the array (either left or right) where the left bound value
        of that portion is greater than the right bound value because it surely
        will contain the minimum value of the array.
        """
        l = 0
        r = len(nums) - 1
        min_numb = nums[0]

        while l <= r:
            # considered portion hasn't been rotated -> left elem is the minimum of the whole array
            if nums[l] <= nums[r]:
                return min(nums[l], min_numb)

            m = l + (r - l) // 2
            min_numb = min(min_numb, nums[m])
            if nums[l] <= nums[m]:  # the min lies in [m+1, n)
                l = m + 1
            else:  # the min lies in [l, r-1]
                r = m - 1

        return min_numb
