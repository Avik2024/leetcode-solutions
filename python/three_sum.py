from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in the array which gives the sum of zero.

        Time Complexity: O(n^2), where n is the length of nums.
          - Sorting takes O(n log n).
          - Two pointers traversal nested inside single loop is O(n^2).
        Space Complexity: O(n) for the output list.

        :param nums: List[int] - Input list of integers
        :return: List[List[int]] - List of triplets that sum to zero
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
