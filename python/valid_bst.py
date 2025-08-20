# Valid Binary Search Tree
# LeetCode Problem: https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low, high):
            # An empty node is valid
            if not node:
                return True
            # The value of the current node must be within the valid range
            if not (low < node.val < high):
                return False
            # Recurse left with updated high, recurse right with updated low
            return (helper(node.left, low, node.val) and 
                    helper(node.right, node.val, high))

        return helper(root, float('-inf'), float('inf'))

"""
Time Complexity: O(n) 
    - Each node is visited once.
Space Complexity: O(n)
    - Recursion stack can go as deep as the height of the tree (worst case skewed tree).
"""
