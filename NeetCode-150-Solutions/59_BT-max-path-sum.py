"""
Given the root of a non-empty binary tree, return the maximum path sum of any
non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
has an edge connecting them. A node can not appear in the sequence more than
once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    The idea behind this problem is to decompose the problem node by node.
    For each node, we can compute the max path sum of its left and right
    children separately and then the total sum accounting the current node.
    The best path sum between the three choices is then kept as the best
    path.
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val

        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0

            # compute the children maximum path sum, ignoring nodes which would negatively
            # impact the path sum
            leftPath = max(dfs(node.left), 0)
            rightPath = max(dfs(node.right), 0)
            maxPath = max(maxPath, leftPath + rightPath + node.val)

            # a parent can only take one branch if this node wants to extend upward
            return node.val + max(leftPath, rightPath)
        dfs(root)
        return maxPath
