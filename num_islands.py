class Solution:
    def numIslands(self, grid):
        """
        Returns the number of islands in the given 2D grid.

        Time Complexity: O(m * n)
            - Each cell is visited at most once, where m is the number of rows and n is the number of columns.
        Space Complexity: O(m * n)
            - In the worst case (when the entire grid is land), the recursion stack for DFS could be O(m * n).
        """
        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # Mark as visited
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
