# Valid Binary Search Tree - Iterative Solution
# LeetCode Problem: https://leetcode.com/problems/validate-binary-search-tree/

# Time Complexity: O(n) -> each node is visited once
# Space Complexity: O(h) -> stack stores nodes up to tree height (h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = float('-inf')
        cur = root 

        while stack or cur:
            # Go left as far as possible
            while cur:
                stack.append(cur)
                cur = cur.left 

            # Process current node
            cur = stack.pop()
            if cur.val <= prev:
                return False 
            prev = cur.val

            # Move to right subtree
            cur = cur.right

        return True
