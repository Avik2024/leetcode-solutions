from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array output such that output[i] is equal to the product 
        of all the elements of nums except nums[i] without using division.

        Time Complexity: O(n), where n is the length of nums.
          - We make two passes through the array.
        Space Complexity: O(1) excluding the output array.
          - We use output array for results and two variables for left and right products.

        :param nums: List[int] - Input array of integers
        :return: List[int] - Product array except self
        """
        n = len(nums)
        output = [1] * n

        # left product accumulation
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # right product accumulation
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
