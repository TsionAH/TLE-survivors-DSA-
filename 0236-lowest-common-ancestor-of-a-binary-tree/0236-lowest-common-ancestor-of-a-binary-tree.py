# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,q,p):
            if node is None :
                return None
            if node == q or node == p:
                return node
            left = dfs(node.left,q,p)
            right =dfs(node.right,q,p)
            if left is None and right is None:
                return None
            if left is None:
                return right
            if right is None :
                return left
            else:
                return node
        return dfs(root,p,q)
