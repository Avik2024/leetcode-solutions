from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the list contains any duplicates.
        
        Time Complexity: O(n), where n is the length of nums.
          - Inserting and checking in a set is O(1) on average, done n times.
        Space Complexity: O(n), for storing elements in the set in the worst case.
        
        :param nums: List[int] - The list of integers to check
        :return: bool - True if duplicates exist, False otherwise
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
