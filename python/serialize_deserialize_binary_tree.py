from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Encode a tree node to a single string
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    # Decode a single string to tree node
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        values = data.split(",")
        
        # Special case: TreeNode is completely empty
        if values[0] == "null":
            return None
        
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root


"""
Time Complexity: O(n) 
    - Each node is visited once during serialization and once during deserialization.
Space Complexity: O(n) 
    - Extra space used for queue and result list storing n values.
"""
