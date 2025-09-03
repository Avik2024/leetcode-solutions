from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]   # start with the first element
        
        for i in range(1, len(nums)):
            # either extend the current subarray or start new
            cur = max(nums[i], cur + nums[i])
            res = max(res, cur)
        
        return res
#Time complexcity -  O(n)
#Space Complexity - O(1)

