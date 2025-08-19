"""
You are given an array of integers nums containing n + 1 integers. Each integer
in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or
more times. Return the integer that appears more than once.
"""


class Solution1:  # modifies the elements in the array
    def findDuplicate(self, nums: List[int]) -> int:
        """
        The idea is that, because we know that the contains n+1 elements
        and each element is in range [1, n], instead of using a separate
        hashset which would require additional space, we use the input
        array itself to keep track of which elements have already been 
        "seen" in the array.
        """
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] < 0:
                return idx + 1
            nums[idx] *= -1

        return -1


class Solution2:  # doesn't modify the input array, still achieves O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        """
        This problem can be solved without modifying the input list with one key
        intuition:
        - Because each element is a valid index in the input array, we can see
        this problem as finding a loop in graph terms by treating indexes as nodes
        and the corersponding value as the pointer to the next node:
            input array: [3, 1, 3, 4, 2]
        1. from index 0 -> nums[0] = 3
        2. from index 3 -> nums[3] = 4
        3. from index 4 -> nums[4] = 2
        4. from index 2 -> nums[2] = 3 --> cycle detected i.e. 3 is the duplicate

        With this intuition, we can leverage the Floyd's Tortoise & Hare cycle detection
        algorithm to find the cycle start i.e.: duplicate number.
        """
        slow, fast = 0, 0

        # finding the point within the cycle where the two pointers meet
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0  # == fast
        # reset one of the two at the start and move both one at a time
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow2 == slow:
                break

        return slow2
