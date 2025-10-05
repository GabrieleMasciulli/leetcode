"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates
that you must take course b first if you want to take course a.

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.
There are a total of numCourses courses you are required to take, labeled from 0
to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there
are many valid answers, return any of them. If it's not possible to finish all
courses, return an empty array.
"""

from collections import defaultdict, deque


class Solution:
    """
    The idea to solve this problem is to use topological sort such that to create
    a valid order of courses to take in order to satisfy all prerequisites.
    First we assign the number of prerequisites each course has.
    Then, we start "taking" those courses which have 0 prerequisites and
    decrease the prereq count (in degree) for each course which depended
    on it and add it to the node queue to process if it has a 0 prerequisite
    dependency count.
    We iteratively apply this process until either:
    1. No more nodes are left to be processed and the list of course taken can
        be returned
    2. If no more nodes are left in the queue but some remain unprocessed then
        a cycle is present and an empty list is returned.
    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # b -> [a..] key: course -> value: list of courses that depend on it
        adj = defaultdict(list)
        in_degree = [0] * numCourses  # number of prerequisites for each course

        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        # initially adding courses with in_degree == 0 to the queue
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while q:
            prereq = q.popleft()
            result.append(prereq)

            # decrease in_degree of all courses that depended on the one added to the result
            for course in adj[prereq]:
                in_degree[course] -= 1

                if in_degree[course] == 0:
                    q.append(course)

        return result if len(result) == numCourses else []
