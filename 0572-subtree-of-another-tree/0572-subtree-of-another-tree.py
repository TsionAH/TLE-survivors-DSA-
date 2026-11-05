# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isTree(q,p):
                if q is None and p is None:
                    return True
                elif (q is None) or (p is None):
                    return False
                elif q.val != p.val:
                    return False
                return (isTree(q.left,p.left) and isTree(q.right,p.right))
        if root is None:
            return False
        if subRoot is None:
            return True
       
        if root.val == subRoot.val :
            if isTree(root,subRoot):
                return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
            