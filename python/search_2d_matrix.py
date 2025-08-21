from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        size = m * n
        left, right = 0, size - 1
        while left <= right:
            mid = left + (right - left) // 2
            row, col = divmod(mid, n)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Time Complexity: O(log(m * n))
# Space Complexity: O(1)
