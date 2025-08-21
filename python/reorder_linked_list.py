from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders list to L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
        Time Complexity: O(n) - each node visited a constant number of times
        Space Complexity: O(1) - in-place reordering without extra data structures
        """
        if not head or not head.next or not head.next.next:
            return  # No need to reorder for 0, 1, or 2 nodes

        # Step 1: Find the middle (slow will be at midpoint)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Split the list into two halves

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
