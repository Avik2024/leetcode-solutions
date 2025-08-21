from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list has a cycle using Floyd’s Tortoise and Hare algorithm.
        Time Complexity: O(n) - each node is visited at most once
        Space Complexity: O(1) - uses constant extra space
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
