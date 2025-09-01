# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        elif not root:
            return root
        elif p.val < root.val and q.val > root.val:  # root is the lca
            return root
        elif p.val == root.val or q.val == root.val:
            return root
        elif p.val > root.val:  # q is hence greater than root.val
            return self.lowestCommonAncestor(root.right, p, q)

        return self.lowestCommonAncestor(root.left, p, q)
