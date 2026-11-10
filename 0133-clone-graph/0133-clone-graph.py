"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        adj = {}
        
        def dfs(node):
            if node in adj:
                return adj[node]
            newNode = Node(node.val)
            adj[node] = newNode
            for val in node.neighbors:
             
                newNode.neighbors.append(dfs(val))
            return newNode
        return dfs(node)