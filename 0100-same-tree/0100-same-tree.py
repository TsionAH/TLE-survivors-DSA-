# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if q is None and p is None:
            return True
        
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        
        return (self.isSameTree(q.left , p.left) and
        self.isSameTree(q.right,p.right))
            