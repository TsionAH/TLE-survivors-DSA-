# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        max_sum = float('-inf')
        ans = 0
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        queue = deque([root])
        count = 0
        while queue:
            level = len(queue)
            sum_each = 0
            
            for i in range(level):
                node = queue.popleft()
                sum_each += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count += 1
            if sum_each > max_sum:
                ans = count
                max_sum = max(max_sum,sum_each)
            
        return ans
