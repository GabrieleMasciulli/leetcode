"""
Given the roots of two binary trees p and q, return true if the trees are
equivalent, otherwise return false.

Two binary trees are considered equivalent i they share the exact same
structure and the nodes have the same values.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        equivalent = True

        def dfs(n1, n2):
            nonlocal equivalent
            if (not n1) ^ (not n2):  # xor
                equivalent = False
            if not n1 or not n2:
                return

            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)
            equivalent = equivalent and n1.val == n2.val

        dfs(p, q)
        return equivalent
