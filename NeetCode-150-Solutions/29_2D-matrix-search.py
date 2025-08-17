class Solution:
    """
    You are given an m x n 2-D integer array matrix and an integer target.

    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.
    Return true if target exists within matrix or false otherwise.

    Can you write a solution that runs in O(log(m * n)) time?
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # rows
        n = len(matrix[0])  # columns

        l = 0
        r = m - 1

        # iterating over the last column of the matrix
        # such that to find the right row in which to search
        # the target (if any). -> O(log m)
        while l <= r:
            middle_row = l + (r - l) // 2
            lastElem = matrix[middle_row][-1]
            firstElem = matrix[middle_row][0]

            if target > lastElem:
                l = middle_row + 1
            elif target < firstElem:
                r = middle_row - 1
            else:  # target is in the current row -> apply simple binary search on the current row
                l = 0
                r = n - 1

                while l <= r:  # -> O(log n)
                    middle_col = l + (r - l) // 2
                    middle_elem = matrix[middle_row][middle_col]

                    if target > middle_elem:
                        l = middle_col + 1
                        print("l", l)
                    elif target < middle_elem:
                        r = middle_col - 1
                    else:
                        return True
        return False
