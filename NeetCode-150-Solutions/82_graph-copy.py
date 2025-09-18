"""
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is
a mapping of nodes to lists, used to represent a finite graph. Each list
describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total
number of nodes in the graph. The index of each node within the adjacency list
is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.
"""

# Definition for a Node.


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Starting from the root node in the graph, the idea to tackle this problem is
    to use a BFS approach by adding all neighbors to the queue and popping one
    node at a time to reconstruct the deepcopy as elements are popped.
    When adding elements, we make sure to avoid re-adding nodes which were already
    processed through by keeping track of expanded nodes.
    """

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}  # maps node values to its reference node object
        nodes[node.val] = Node(node.val)  # adding root (1)
        q = deque([node])  # queue

        while q:
            n = q.popleft()

            for neigh in n.neighbors:
                newNeigh = None

                if neigh.val not in nodes:  # create node
                    q.append(neigh)
                    newNeigh = Node(neigh.val)
                    nodes[neigh.val] = newNeigh
                else:
                    newNeigh = nodes[neigh.val]

                nodes[n.val].neighbors.append(newNeigh)

        return nodes[1]
