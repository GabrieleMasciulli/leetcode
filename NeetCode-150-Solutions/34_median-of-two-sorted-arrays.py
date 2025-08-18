class Solution:
    """
    You are given two integer arrays nums1 and nums2 of size m and n
    respectively, where each is sorted in ascending order. 

    Return the median value among all elements of the two arrays.
    Your solution must run in  O(log(m+n)) time.
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The idea to solve this problem is to divide both arrays in two parts
        such that all the elements in the left (combined) half are smaller or
        equal to all the elements in the (combined) right half by keeping the 
        constraint that the size of the left half (same reasoning goes for the right half)
        should correspond to (m+n)//2 when (m+n) is even and (m+n+1)//2 when (m+n) is odd.

        If we manage to have this constraint satisfied, then the median will be:
        - the max of the left half if (m+n) is odd
        - the mean between the max of the left and the max of the right halves.

        A valid "cut" given `i` the cut for nums1 and `j` the cut for nums2, is found
        when, the size constraints are satisfied and, the following condition hold:
                               L1 <= R2 && L2 <= R1 
        where:
        - L1 is the biggest number in the left half of the first array i.e. nums1[i-1] or -inf if i=0
        - L2 is nums2[j-1] or -inf if j=0
        - R1 is the smallest number in the right side of the first array i.e. nums1[i] or +inf if i=m
        - R2 is nums2[j] or +inf if j=n

        Then, we perform binary search over the first array (through i) and compute the second index 
        j based on the value of i:
        - Given i then the total left side should need (m + n + 1)//2 elements meaning the cut in 
        the second array should be at j = total_left - i

        1. When L1 > R2 it means we took too many elements from nums1 --> we move i to the left
        2. When L2 > R1 it means we took too few elements from nums1 --> we move i to the right
        """
        m, n = len(nums1), len(nums2)

        if (m > n):
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, m
        total_left = (m + n + 1) // 2
        while l <= r:
            i = l + (r - l) // 2
            j = total_left - i

            L1 = nums1[i-1] if i > 0 else -float('inf')
            L2 = nums2[j-1] if j > 0 else -float('inf')
            R1 = nums1[i] if i < m else float('inf')
            R2 = nums2[j] if j < n else float('inf')

            if L1 <= R2 and L2 <= R1:
                return max(L1, L2) if (m+n) % 2 == 1 else (max(L1, L2) + min(R1, R2)) / 2
            elif L1 > R2:
                r = i - 1
            else:
                l = i + 1

        return
