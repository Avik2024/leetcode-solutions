from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Copies a linked list with random pointers.
        Time Complexity: O(n) - traverses list a constant number of times
        Space Complexity: O(1) - modifies list in-place without extra hash maps
        """
        if not head:
            return None

        # Step 1: Clone and interleave nodes
        cur = head
        while cur:
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next

        # Step 2: Set random pointers for the clones
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: Separate the two lists
        cur = head
        copy_head = head.next
        while cur and cur.next:
            copy = cur.next
            cur.next = copy.next
            cur = cur.next
            if cur:
                copy.next = cur.next

        return copy_head
