import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # Max heap (store negative values)
        self.right = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to max heap (as negative for max heap behavior)
        heapq.heappush(self.left, -num)
        # Balance: move the max from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # Maintain size property: left heap can have equal or 1 more element than right
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left + self.right) / 2

# Time Complexity:
# addNum: O(log n) due to heap push/pop operations
# findMedian: O(1) to read the top elements

# Space Complexity:
# O(n) to store all elements across two heaps
