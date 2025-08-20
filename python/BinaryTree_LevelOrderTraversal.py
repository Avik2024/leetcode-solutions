from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            node_size = len(queue)
            level_nodes = []   # ✅ fixed typo (was levels_nodes)
            
            for _ in range(node_size):
                node = queue.popleft()
                level_nodes.append(node.val)  # ✅ fixed typo (was levels_node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_nodes)
        
        return res   # ✅ fixed typo (was retrun)

"""
Time Complexity: O(n)
- Each node is processed once, so total operations = n.

Space Complexity: O(n)
- In the worst case, the queue can hold all nodes at the last level of the tree.
"""
