# Kth Smallest Element in a BST
# Iterative Inorder Traversal

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while True:
            # Go to the left as far as possible
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            # If we reached the kth smallest
            if count == k:
                return current.val

            # Move to the right subtree
            current = current.right


"""
Time Complexity: O(n)  -> In worst case we may traverse all nodes
Space Complexity: O(n) -> Stack stores up to n nodes in skewed tree
"""
