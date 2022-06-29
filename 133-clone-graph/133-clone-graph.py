"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        
        copyNodes={}
        
        def dfs(node):
            copyNodes[node]=Node(node.val)
            
            for nei in node.neighbors:
                if nei not in copyNodes:
                    dfs(nei)
                copyNodes[node].neighbors.append(copyNodes[nei])
        
        dfs(node)
        return copyNodes[node]
            
            
        
       
            
            
        