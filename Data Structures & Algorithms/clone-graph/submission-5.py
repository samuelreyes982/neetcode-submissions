"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen=set()
        dic={}
        def dfs(current_node):
            #print(f'node {current_node.val}.   prev {prev}')
            #create current node
            if current_node in dic:
                return dic[current_node]
            #key=current_node.val
            
            new_node=Node()
            new_node.val=current_node.val
            dic[current_node]=new_node
            #seen.add(key)

            #print(f'node nieghbros {node.neighbors}')
            for neighbor in current_node.neighbors:
                #print(neighbor.val)
                #print(f'len neighbors {len(n)}')
                
                new_node.neighbors.append(dfs(neighbor)) 
            
            #new_node.neighbors.append(prev) 

            return new_node   
        if not node:
            return node
        else:
            return dfs(node)