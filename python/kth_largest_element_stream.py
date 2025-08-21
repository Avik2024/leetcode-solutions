import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums[:]  # copy of initial list
        heapq.heapify(self.minheap)  # O(n)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # push the new value
        heapq.heappush(self.minheap, val)
        # if heap grew beyond k, remove smallest
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        # top of minheap is kth largest
        return self.minheap[0]

# Time Complexity:
# 1. Constructor (__init__)
#    a. heapify on nums -> O(n), where n is length of nums
#    b. Removing excess elements -> O((n - k) log n)
#    c. Overall ~ O(n) for large n relative to k
# 2. add(val)
#    a. heappush -> O(log k)
#    b. heappop (optional) -> O(log k)
#    c. Total per add: O(log k)

# Space Complexity:
# 1. Stores at most k elements in the heap -> O(k)
# 2. Copy of nums optional, but here consumes O(n) initially
