"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees are also binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        traversed = 0

        def dfs(node):  # applied inorder traversal to count nodes as left -> curr -> right
            nonlocal res
            nonlocal traversed

            if not node:
                return

            # left traversal
            dfs(node.left)
            # curr count
            traversed += 1

            # found Kth smallest, saving result
            if traversed == k:
                res = node.val
                return res

            # right traversal
            dfs(node.right)

        dfs(root)
        return res
