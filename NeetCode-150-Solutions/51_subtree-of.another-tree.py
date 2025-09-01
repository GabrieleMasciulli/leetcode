"""
Given the roots of two binary trees root and subRoot, return true if there is a
subtree of root with the same structure and node values of subRoot and false
otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and
all of this node's descendants. The tree tree could also be considered as a
subtree of itself.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSame(self, p, q):
        if (not p) ^ (not q):
            return False
        elif (not p) and (not q):
            return True

        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root) ^ (not subRoot):
            return False
        elif not root and not subRoot:
            return True
        if root.val == subRoot.val:
            return self.isSame(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
