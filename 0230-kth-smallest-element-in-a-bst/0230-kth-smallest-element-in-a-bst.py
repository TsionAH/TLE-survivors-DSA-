# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        result = 0
        def dfs(node):
            nonlocal result,k
            if node is None:
                return 0
            
            dfs(node.left)
            k -= 1
            if k == 0:
                result = node.val
                
            dfs(node.right)
        dfs(root)
        return result 
