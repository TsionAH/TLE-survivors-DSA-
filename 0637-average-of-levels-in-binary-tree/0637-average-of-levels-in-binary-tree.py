# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        result = []
        if root is None:
            return []
        queue = deque([root])
        while queue:
            level = len(queue)
            value = 0
            for i in range(level):
                node = queue.popleft()
                value += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            avg = value/level
            result.append(avg)
        return result