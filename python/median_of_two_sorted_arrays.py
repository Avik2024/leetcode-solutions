from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Optimized Approach with Binary Search:
        - Partition arrays for median calculation in O(log(min(n, m))) time.
        - Time Complexity: O(log(min(n, m)))
        - Space Complexity: O(1)
        """
        A, B = nums1, nums2
        if len(A) > len(B):  # ensure A is the smaller array
            A, B = B, A
        n, m = len(A), len(B)
        total = n + m
        half = total // 2
        
        left, right = 0, n
        while left <= right:
            i = (left + right) // 2    # A's partition
            j = half - i               # B's partition

            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < n else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < m else float("inf")
            
            # Check correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1
