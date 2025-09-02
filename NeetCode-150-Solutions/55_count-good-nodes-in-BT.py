"""
Within a binary tree, a node x is considered good if the path from the root of
the tree to the node x contains no nodes with a value greater than the value of
node x.

Given the root of a binary tree root, return the number of good nodes within the
tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0  # root is always considered a `good node`

        def dfs(node, largest):
            nonlocal count

            count = count + 1 if node.val >= largest else count
            largest = max(largest, node.val)

            if node.left:
                dfs(node.left, largest)
            if node.right:
                dfs(node.right, largest)

        dfs(root, root.val)

        return count
