# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, they are the same
        if not p and not q:
            return True
        # If one is None or values don't match, not the same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Time Complexity: O(n)  # we visit each node once
Space Complexity: O(h)  # recursion stack where h = height of tree
"""
