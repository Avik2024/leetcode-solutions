from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        # Build the graph as an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False  # Found a cycle
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue  # Skip the node we came from
                if not dfs(neighbor, node):
                    return False
            return True
        
        # Start DFS from node 0
        if not dfs(0, -1):
            return False
        
        # Check if all nodes were visited (i.e., the graph is connected)
        return len(visited) == n


# Time Complexity: O(n + e)
#   - n: number of nodes
#   - e: number of edges
#   - We visit every node once and every edge once in the DFS

# Space Complexity: O(n + e)
#   - O(n) for the visited set and recursion stack (in worst-case linear depth)
#   - O(e) for the adjacency list representing the graph
