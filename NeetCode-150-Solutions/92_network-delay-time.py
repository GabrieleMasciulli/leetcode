"""
You are given a network of n directed nodes, labeled from 1 to n. You are also given times,
a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal.
If it is impossible for all the nodes to receive the signal, return -1 instead.


"""

from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)  # adjacency list with associated weights

        # building weighted adj. list.
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        def dijkstra(adj, src, V):
            dist = [float("inf")] * V  # distances from source to each vertex
            dist[src] = 0  # distance from source to source is 0

            minHeap = []
            heapq.heappush(
                minHeap, (0, src)
            )  # starting node with 0 distance (src->src == 0)

            while minHeap:
                d, u = heapq.heappop(minHeap)

                # avoids multiple relaxations
                if d > dist[u]:
                    continue

                for v, t in adj[u]:
                    if dist[u] + t < dist[v]:
                        dist[v] = dist[u] + t
                        heapq.heappush(minHeap, (dist[v], v))
            return dist

        distances = dijkstra(adj, k - 1, n)

        for d in distances:
            if d == float("inf"):
                return -1
        return max(distances)
