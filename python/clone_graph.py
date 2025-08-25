class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def clone(node):
            if not node:
                return None
            
            if node in visited:
                return visited[node]   # ✅ Already cloned, return it
            
            # Create a clone of the current node
            clone_node = Node(node.val)
            visited[node] = clone_node   # ✅ Map original ➝ clone

            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))
            
            return clone_node 
        
        return clone(node)


"""
⏱️ Time Complexity:  O(V + E)
- Each node is visited exactly once (V = number of vertices).
- Each edge is processed once when traversing neighbors (E = number of edges).

💾 Space Complexity: O(V)
- Hash map `visited` stores a clone for every original node → O(V).
- Recursion stack depth can go up to O(V) in the worst case (graph shaped like a line).
"""
