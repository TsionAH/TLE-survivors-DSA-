# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if node is None:
                return None
            left = dfs(node.left)
            count += 1
            if left is  not None:
                return left
            if count == k:
                return node.val
            return dfs(node.right)
        return dfs(root)