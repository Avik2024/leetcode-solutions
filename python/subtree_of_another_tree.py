# Subtree of Another Tree
# LeetCode Problem

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Checks if subRoot is a subtree of root
        """

        if not subRoot:  # An empty tree is always a subtree
            return True
        if not root:  # If root is None but subRoot is not, return False
            return False
        if self.isSameTree(root, subRoot):
            return True
        # Recurse left and right
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two trees are identical
        """
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False


"""
Time Complexity:
- In the worst case, for each node in `root` (n nodes), 
  we may compare with `subRoot` (m nodes). 
- So, O(n * m).

Space Complexity:
- Recursion depth can go up to O(n) in the worst case (skewed tree). 
- For comparison calls, O(m).
- Total: O(n + m)
"""
