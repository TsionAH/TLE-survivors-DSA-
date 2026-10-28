# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        max_deptp = 0
        def dfs(node,count=0):
            
            if node is None:
                nonlocal max_deptp
                max_deptp = max(max_deptp,count)
                return max_deptp
            
            dfs(node.left,count+1)
            dfs(node.right,count + 1)
        dfs(root)
        return max_deptp 
            