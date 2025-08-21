class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reversedList(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list.
    Time Complexity: O(n) - traverses all nodes once
    Space Complexity: O(1) - in-place reversal with constant space
    """
    prev = None
    curr = head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev
