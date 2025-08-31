"""
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and
right subtrees of every node differ in height by no more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            if not node:
                return 0
            nonlocal balanced

            left_h = dfs(node.left)
            right_h = dfs(node.right)
            balanced = balanced and abs(left_h - right_h) <= 1
            return 1 + max(left_h, right_h)

        dfs(root)
        return balanced
