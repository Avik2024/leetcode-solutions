# Lowest Common Ancestor in a Binary Search Tree (BST)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            # If both nodes are greater, LCA is in right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both nodes are smaller, LCA is in left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # This is the split point, so this node is the LCA
                return curr


"""
Time Complexity: O(h)
- In a balanced BST, height h = log(n)
- Worst case (skewed tree), h = n

Space Complexity: O(1)
- We are only using a pointer 'curr'
"""
