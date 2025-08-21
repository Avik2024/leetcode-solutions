from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Uses Floyd's Tortoise and Hare (Cycle Detection) to find duplicate number.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Phase 1: Find the intersection point of the two runners.
        slow = nums[0]
        fast = nums
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle, which is the duplicate number.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
