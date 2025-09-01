"""
Given a binary tree root, return the level order traversal of it as a nested
list, where each sublist contains the values of nodes at a particular level in
the tree, from left to right.
"""
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])

        while queue:
            queueLen = len(queue)
            level = []

            while queueLen > 0:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                queueLen -= 1
            res.append(level)

        return res
