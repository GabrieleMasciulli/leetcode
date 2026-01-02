"""
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.
"""

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        root = self.parent[x]

        if root != x:
            self.parent[x] = self.find(self.parent[root])
            return self.parent[x]
        return x

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return False  # belong to the same set

        xRank, yRank = self.rank[xRoot], self.rank[yRoot]

        if yRank < xRank:
            self.parent[yRoot] = xRoot
        elif xRank > yRank:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[yRoot] += 1
        return True


class Solution:
    """
    We can solve this problem by looking at points as if they were
    nodes in a graph.
    What the problem is asking for is to find the minimum-spanning tree
    (MST) of the given points.
    We can solve this problem by simply using Kruskal's algorithm
    """

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = UnionFind(len(points))
        edges = []
        added_edges = 0
        tot_cost = 0
        pt_to_id = defaultdict(int)

        # mapping each point to an integer id
        i = 0
        for x, y in points:
            pt_to_id[(x, y)] = i
            i += 1

        # generating all possible edges
        for xi, yi in points:
            for xj, yj in points:
                if xi == xj and yi == yj:
                    continue

                manh_dist = abs(xi - xj) + abs(yi - yj)
                edges.append([manh_dist, (xi, yi), (xj, yj)])  # (dist, p1, p2)

        edges = sorted(edges)

        for d, p1, p2 in edges:  # p as (x, y)
            if not dsu.union(
                pt_to_id[p1], pt_to_id[p2]
            ):  # arc p1 -> p2 would generate a cycle, skipping
                continue

            added_edges += 1
            tot_cost += d

            if added_edges == len(points) - 1:  # MST has V-1 edges
                return tot_cost

        return tot_cost
