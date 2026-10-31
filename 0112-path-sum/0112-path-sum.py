# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def dfs(node,target,value):
            if node is None:
                return False
            value += node.val
            if node.left is None and node.right is None :
                return value == target
            left = dfs(node.left,target,value)
            right = dfs(node.right,target,value)
            
            return (left or right)
        return dfs(root,targetSum,0)
            
            