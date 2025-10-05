"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree.
"""


from collections import defaultdict


class Solution:
    """
    Given the definition of Tree i.e.: an undirected graph with no cycles
    where all the nodes are connected as one component and any two nodes are
    reachable by exactly one path, the idea to solve this problem is the
    following:
    1. We construct an adjacency list
    2. Starting from any node in the graph, we do a DFS on the adjacent nodes
    and check at each recursion call if the current node was already visited
    except the parent node of the current node (as the edges are undirected).
    """

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n or len(edges) < n-1:
            return False

        adj = defaultdict(set)

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        def dfs(node, parent, visited):
            visited.add(node)

            for neigh in adj[node]:
                if neigh != parent and neigh in visited:
                    return False

                if neigh not in visited and not dfs(neigh, node, visited):
                    return False
            return True

        visited = set()
        dfs(0, -1, visited)

        return len(visited) == n
