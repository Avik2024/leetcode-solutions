# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            if not node:
                return []
            return [node.val] + preorder(node.left) + preorder(node.right)
        return preorder(root)

# Time Complexity - O(n)
# Space Complexity - O(log n) average, O(n) worst case (skewed tree)
