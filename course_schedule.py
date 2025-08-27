from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be completed given prerequisites.

        A course schedule is valid (can finish all courses) if there is no cycle
        in the course dependency graph (i.e., the graph is a Directed Acyclic Graph - DAG).

        Parameters:
        - numCourses (int): total number of courses labeled from 0 to numCourses - 1
        - prerequisites (List[List[int]]): list of [course, prerequisite] pairs

        Returns:
        - bool: True if all courses can be completed, False otherwise

        Time Complexity:
        - O(n + e), where n = numCourses and e = number of prerequisites
          - We visit every course once and every edge once.

        Space Complexity:
        - O(n + e)
          - O(n) for indegree array and queue
          - O(e) for adjacency list representation of the graph
        """

        graph = defaultdict(list)           # Adjacency list to represent course dependencies
        indegrees = [0] * numCourses        # Count of prerequisites for each course

        # Build the graph and fill indegrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)    # prereq → course
            indegrees[course] += 1          # Increase indegree count of the course

        # Initialize queue with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        completed_count = 0

        # Process courses in topological order
        while queue:
            course = queue.popleft()
            completed_count += 1

            for successor in graph[course]:
                indegrees[successor] -= 1   # Remove dependency
                if indegrees[successor] == 0:
                    queue.append(successor)

        # If all courses were completed, return True
        return completed_count == numCourses

