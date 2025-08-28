class DSU:
    def __init__(self, n: int):
        # Initially, each node is its own parent (self loop)
        self.parent = list(range(n))   # O(n) space
        self.rank = [1] * n            # O(n) space

    def find(self, node: int) -> int:
        # Iterative path compression
        cur = node 
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]  # Path compression
            cur = self.parent[cur]
        return cur

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)  # O(α(n)) time each
        if pu == pv:
            return False  # Already connected
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu  # Ensure higher-rank root stays

        self.parent[pv] = pu  # Union by rank
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        components = n
        for u, v in edges:
            if dsu.union(u, v):  # Union returns True if two components were merged
                components -= 1
        return components

# -----------------------------------------------------
# ⏱️ Time Complexity:
# - Initialization: O(n)
# - Each union and find operation: O(α(n)) → nearly constant time due to path compression
# - For m edges: O(m * α(n))

# So total: O(n + m * α(n)), where:
# - n = number of nodes
# - m = number of edges
# - α(n) = inverse Ackermann function (very slow-growing)

# 📦 Space Complexity:
# - O(n) for parent and rank arrays
