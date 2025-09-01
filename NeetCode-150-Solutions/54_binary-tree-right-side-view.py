"""
You are given the root of a binary tree. Return only the values of the nodes
that are visible from the right side of the tree, ordered from top to bottom.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, height):
            if not node:
                return
            if len(res) == height:  # need to save the item for the current level
                res.append(node.val)

            dfs(node.right, height + 1)
            dfs(node.left, height + 1)

        dfs(root, 0)
        return res
