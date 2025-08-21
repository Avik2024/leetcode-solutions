from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # Base case: all chars matched
            if i == len(word):
                return True
            # Boundary & char match check
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[i]):
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  # mark visited

            # Explore all 4 directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))
            
            board[r][c] = temp  # backtrack
            return found

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True

        return False

# Complexity:
# Time: O(M*N*4^L) where M,N = board dimensions, L = word length
# Space: O(L) for recursion stack
