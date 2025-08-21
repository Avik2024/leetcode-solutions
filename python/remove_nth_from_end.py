from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list.
        Time Complexity: O(n) - one pass to calculate length (implicitly with two pointers)
        Space Complexity: O(1) - only constant extra space used
        """
        dummy = ListNode(-1, head)
        first = second = dummy

        # Move first pointer n + 1 steps ahead to maintain the gap
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the nth node
        second.next = second.next.next

        return dummy.next
