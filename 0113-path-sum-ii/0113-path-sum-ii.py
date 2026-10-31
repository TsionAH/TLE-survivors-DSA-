# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        def dfs(node,target,value,eachList):
            if node is None:
                return 
            value += node.val
            eachList.append(node.val)
            if node.left is None and node.right is None:
                if target == value:
                    result.append(eachList.copy())
            dfs(node.left, target, value,eachList)
            
            dfs(node.right,target,value,eachList)
            eachList.pop()
            

        dfs(root,targetSum,0,[])
        return result
