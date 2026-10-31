# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        
        if root is None:
            return []
        queue = deque([root])
        is_right = False
        while queue:
            level = len(queue)
            level_res= []
            
            for i in range(level):
                each_node = queue.popleft()
                level_res.append(each_node.val)
                if each_node.left:
                    queue.append(each_node.left)
                if each_node.right:
                    queue.append(each_node.right)
            if is_right:
                level_res.reverse()
                    
            result.append(level_res)
            is_right = not is_right
        
        return result
