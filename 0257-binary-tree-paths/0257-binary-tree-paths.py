# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res =[]
        if root is None:
            return []
        def dfs(node,string):
            if node is None:
                return []
            string.append(node.val)
            if node.left is None and node.right is None:
                res.append("->".join(map(str,string)))
            dfs(node.left,string)
            dfs(node.right,string)
            string.pop()
        dfs(root,[])
        return res
                