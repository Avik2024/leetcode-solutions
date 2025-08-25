class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited, prev_height):
            # Out of bounds or already visited or downhill (not allowed in reverse flow)
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prev_height
            ):
                return 
            
            visited.add((r, c))
            
            # Explore 4 directions
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        # 1. DFS from Pacific border (top row, left col)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        # 2. DFS from Atlantic border (bottom row, right col)
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        # Intersection of pacific and atlantic sets
        result = list(pacific & atlantic)
        return result


"""
TIME COMPLEXITY:
---------------
- Each cell (r, c) can be visited at most once by Pacific DFS and once by Atlantic DFS.
- So total DFS traversals = O(m * n), where m = rows, n = cols.
- DFS itself explores at most 4 directions per cell → O(4 * m * n) ≈ O(m * n).
✅ Overall Time Complexity: O(m * n)

SPACE COMPLEXITY:
----------------
- Recursive DFS call stack depth: O(m * n) in worst case (if all cells are visited in one path).
- Visited sets (pacific, atlantic): O(m * n).
✅ Overall Space Complexity: O(m * n)
"""
