"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates
that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0
to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # key (course) -> [...] (list of courses needed to take to attend key)
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()  # courses marked as non-cyclical
        path = set()  # current prerequisite recursion stack

        def dfs(course):
            if course in visited:
                return True
            if course in path:
                return False

            path.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            visited.add(course)
            return True

        # for each course we check if there is a prerequisite cycle
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
