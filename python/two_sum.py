from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices of values in nums that add up to target.

        Time Complexity: O(n), where n is the length of nums.
          - Each lookup and insertion in the dictionary is O(1) on average.
        Space Complexity: O(n), for storing elements in the dictionary.

        :param nums: List[int] - Input list of integers
        :param target: int - Target sum
        :return: List[int] - Indices of the two numbers that add to target
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # If no solution found, behavior depends on problem statement.
        # Usually, there is always exactly one solution.
        return []
