"""
You are given two integer arrays preorder and inorder.

- preorder is the preorder traversal of a binary tree
- inorder is the inorder traversal of the same tree
- Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.


"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        i, n = 0, len(inorder)  # == len(preorder)

        while i < n:
            val = inorder[i]

            if not val in indices:
                indices[val] = i

            i += 1

        i = 0

        def dfs(left, right):
            if left > right:
                return None

            nonlocal i
            nonlocal indices

            root_val = preorder[i]
            root_idx = indices[root_val]
            i += 1

            # recursively building left sub-tree
            left_tree = dfs(left, root_idx - 1)
            # recursively building right sub-tree
            right_tree = dfs(root_idx + 1, right)

            return TreeNode(root_val, left_tree, right_tree)

        return dfs(0, n - 1)
