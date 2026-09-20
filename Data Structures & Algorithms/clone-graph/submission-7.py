"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        '''

        cloning undirected graph we can use dictionary
        '''

        dic={}

        def clone(existing_node):
            #we already have saved it
            if existing_node in dic:
                return dic[existing_node]
            #cloning old one into a new object
            copy_node= Node(existing_node.val)
            
            dic[existing_node]=copy_node
            

            

            for existing_neighbor in existing_node.neighbors:
                copy_node.neighbors.append(clone(existing_neighbor))
            
            return copy_node
        if node==None:
            return None
        else:
            return clone(node)
        