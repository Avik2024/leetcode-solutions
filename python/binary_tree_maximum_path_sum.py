# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSumUtil(self, root: Optional[TreeNode], res: list[int]) -> int:
        # Base Case
        if not root:
            return 0

        # Calculate the maximum path sum for left and right subtree
        l = max(0, self.maxPathSumUtil(root.left, res))
        r = max(0, self.maxPathSumUtil(root.right, res))

        # Update the result with maximum path sum using current node
        res[0] = max(res[0], l + r + root.val)

        # Return the maximum path sum in one side (used for parent computation)
        return root.val + max(l, r)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialized as very small value
        res = [float('-inf')]
        self.maxPathSumUtil(root, res)
        return res[0]


"""
Time Complexity: O(n) 
    - Each node is visited exactly once.
Space Complexity: O(h) 
    - h is the height of the tree (recursion stack).
    - Worst case: O(n) for a skewed tree, O(log n) for a balanced tree.
"""
