# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count = 0
        prefix = {0:1}
        def dfs(node,target,value):
            nonlocal count
            if node is None :
                return
            value += node.val
            prev = value - target

            if prev in prefix:
                count += prefix[prev]
            prefix[value] = prefix.get(value,0)+1
            dfs(node.left,target,value)
            dfs(node.right,target,value)
            prefix[value] -= 1
        dfs(root,targetSum,0)
        return count