"""
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a
sequence of bits so that it can be stored or sent across a network to be
reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure. There is no
additional restriction on how your serialization/deserialization algorithm
should work.

Note: The input/output format in the examples is the same as how NeetCode
serializes a binary tree. You do not necessarily need to follow this format.
"""
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        q = deque([root])
        serialized = []

        while q:
            node = q.popleft()

            # add node to the string
            serialized.append(str(node.val) if node else "null")

            # adding left and right nodes to queue
            if node:
                q.append(node.left)
                q.append(node.right)

        return ','.join(serialized)

    # Decodes your encoded data to tree.

    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if not data:
            return None

        i = 0
        nodes = data.split(',')
        root = TreeNode(nodes[i])
        i += 1
        q = deque([root])

        while q:
            node = q.popleft()
            leftVal = nodes[i]
            rightVal = nodes[i+1]
            i += 2

            if leftVal != 'null':
                leftNode = TreeNode(int(leftVal))
                node.left = leftNode
                q.append(leftNode)
            if rightVal != 'null':
                rightNode = TreeNode(int(rightVal))
                node.right = rightNode
                q.append(rightNode)

        return root
