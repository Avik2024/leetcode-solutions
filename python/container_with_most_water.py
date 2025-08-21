from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculate the maximum amount of water a container can store between two lines.

        Time Complexity: O(n), where n is the number of lines.
          - We use two pointers that move inward only once.
        Space Complexity: O(1), constant extra space.

        :param height: List[int] - heights of vertical lines
        :return: int - maximum water area
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the smaller height inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
