# Maximum Depth of Binary Tree
# Iterative DFS using stack

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]  # (node, current_depth)
        maxDepth = 0

        while stack:
            node, depth = stack.pop()
            maxDepth = max(maxDepth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return maxDepth


"""
Time Complexity: O(n) 
- We visit each node once.

Space Complexity: O(h) 
- Worst case O(n) (skewed tree), Best/Average O(log n) (balanced tree),
  where h = height of the tree.
"""
