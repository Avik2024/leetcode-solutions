from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence.

        Time Complexity: O(n), where n is the number of elements in nums.
          - Uses a set for O(1) lookups.
          - Each element is visited at most twice.
        Space Complexity: O(n) for the set of unique elements.

        :param nums: List[int] - Input unsorted list of integers
        :return: int - Length of the longest consecutive sequence
        """
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            # Only start sequence if num-1 is not present to avoid revisiting sequences
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Extend the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
