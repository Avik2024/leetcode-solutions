import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left


"""
Time Complexity: O(n log m) 
where n = number of piles and m = max bananas in any pile.
This is because binary search runs in O(log m) and for each mid, 
we compute total hours by iterating over all piles.

Space Complexity: O(1), 
as only a few extra variables are used.
"""
