from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                # Minimum value in right half
                left = mid + 1
            else:
                # Minimum value in the left half
                right = mid
        return nums[left]

"""
Time Complexity: O(log n) 
Space Complexity: O(1)
"""
