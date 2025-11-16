"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b]
means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
"""


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        root = self.parent[x]

        if root != x:
            self.parent[x] = self.find(self.parent[root])  # path compression
            return self.parent[x]
        return root

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return False  # x and y already belong to the same set

        xRank, yRank = self.rank[x], self.rank[y]

        if xRank < yRank:  # adding x's subtree under y's
            self.parent[yRoot] = xRoot
        elif yRank < xRank:  # adding 's subtree under x's
            self.parent[xRoot] = yRoot
        else:
            self.parent[xRoot] = yRoot
            self.rank[xRoot] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_components = n
        dsu = DisjointSetUnion(n)

        for u, v in edges:
            if dsu.union(u, v):
                num_components -= 1

        return num_components
