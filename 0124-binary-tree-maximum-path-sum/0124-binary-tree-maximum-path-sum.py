# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if root is None :
            return 0
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if node is None:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            max_sum = max(max_sum,right+node.val+left)
            return node.val + max(left,right)
            
        dfs(root)
        return max_sum
        '''
        first to check starting from node and then going to the tree 
        and having the vaule sum in each step first to ceck each sub tree the right left and its own sum if it is max save at a max and then and then sum up the sub tree and if it gives the max 

        '''