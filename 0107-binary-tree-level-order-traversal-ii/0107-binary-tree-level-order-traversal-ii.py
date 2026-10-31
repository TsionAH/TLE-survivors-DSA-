# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        result = deque([])
        if root is None:
            return []
        queue = deque([root])
        
        while queue:
            level = len(queue)
            each_res = []
            for i in range(level):
                node = queue.popleft()
                each_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.appendleft(each_res)
        return list(result)

        