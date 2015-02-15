# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from copy import copy

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self._visitedNodes = {}
    
    def cloneGraph(self, node):
        if node.label in self._visitedNodes:
            return self._visitedNodes[node.label]
        
        # shallow copy
        clonedNode = copy(node)

        # This registration should be prior to neighbor traversal to avoid infinite loop
        self._visitedNodes[clonedNode.label] = clonedNode

        clonedNode.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        
        return clonedNode

